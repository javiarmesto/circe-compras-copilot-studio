#!/usr/bin/env python3
"""Circe demo: deterministic stdlib calculation, no network or ERP writes."""
import argparse
import csv
import json
from decimal import Decimal, InvalidOperation, ROUND_CEILING
from pathlib import Path
COLUMNS=('item_no','description','location','available_qty','incoming_qty','demand_qty','target_qty','pack_qty','unit_cost','supplier')
QUANTITIES=('available_qty','incoming_qty','demand_qty','target_qty','pack_qty')

def number(raw,field,integer=False,positive=False):
    try: n=Decimal(str(raw).strip())
    except (InvalidOperation,ValueError): raise ValueError(f'{field}: número ausente o inválido')
    if not n.is_finite() or n<0 or (positive and n==0) or n>Decimal('1000000000'):
        raise ValueError(f'{field}: valor fuera del rango admitido')
    if integer and n!=n.to_integral_value(): raise ValueError(f'{field}: se requieren unidades enteras')
    if not integer and n!=n.quantize(Decimal('.01')): raise ValueError(f'{field}: máximo dos decimales')
    return n

def calculate(rows,policy):
    if policy.get('fictional') is not True or policy.get('currency')!='EUR':
        raise ValueError('Se requiere la política ficticia en EUR de la demo')
    for field in ('policy_id','version'):
        if not str(policy.get(field,'')).strip(): raise ValueError(f'Falta {field}')
    threshold=number(policy.get('review_threshold'),'review_threshold')
    results=[]; total=Decimal('0.00')
    counts={}
    for row in rows:
        key=(str(row.get('item_no','')).strip(),str(row.get('location','')).strip())
        counts[key]=counts.get(key,0)+1
    for position,row in enumerate(rows,2):
        r={k:row.get(k,'') for k in ('item_no','description','location','supplier')}
        r.update(row=position,status='INCIDENCIA',need_qty=None,order_qty=None,amount=None,reason='')
        try:
            for field in ('item_no','description','location'):
                if not str(row.get(field,'')).strip(): raise ValueError(f'Falta {field}')
            key=(row['item_no'].strip(),row['location'].strip())
            if counts[key]>1: raise ValueError('Artículo/almacén duplicado: resolver antes de proponer')
            q={k:number(row.get(k,''),k,integer=True,positive=k=='pack_qty') for k in QUANTITIES}
            cost=number(row.get('unit_cost',''),'unit_cost')
            need=max(Decimal(0),q['demand_qty']+q['target_qty']-q['available_qty']-q['incoming_qty'])
            order=(need/q['pack_qty']).to_integral_value(rounding=ROUND_CEILING)*q['pack_qty']
            amount=(order*cost).quantize(Decimal('.01'))
            r.update(need_qty=int(need),order_qty=int(order),amount=str(amount))
            if not order: r.update(status='SIN_COMPRA',reason='Disponible y entradas cubren demanda y objetivo')
            elif not str(row.get('supplier','')).strip(): raise ValueError('Falta supplier: propuesta excluida del total')
            else:
                r.update(status='REVISION_ESPECIAL' if amount>threshold else 'REVISION_NORMAL',reason='Propuesta pendiente de decisión humana')
                total+=amount
        except ValueError as e: r.update(status='INCIDENCIA',reason=str(e))
        results.append(r)
    return dict(fictional=True,policy_id=policy['policy_id'],policy_version=policy['version'],currency='EUR',
                review_threshold=str(threshold),total_proposed=str(total.quantize(Decimal('.01'))),
                proposed_lines=sum(r['status'].startswith('REVISION_') for r in results),
                special_review_lines=sum(r['status']=='REVISION_ESPECIAL' for r in results),
                issue_lines=sum(r['status']=='INCIDENCIA' for r in results),lines=results,
                execution='LOCAL_CALCULATION_ONLY',purchase_orders_created=0)

def safe_cell(value):
    text='' if value is None else str(value)
    return "'"+text if text.lstrip().startswith(('=','+','-','@')) else text

def md(value):
    return str(value if value is not None else '').replace('|','\\|').replace('\n',' ').replace('\r',' ')

def load_rows(path):
    with Path(path).open(encoding='utf-8-sig',newline='') as stream:
        reader=csv.DictReader(stream)
        if reader.fieldnames is None or len(reader.fieldnames)!=len(set(reader.fieldnames)) or set(reader.fieldnames)!=set(COLUMNS):
            raise ValueError('Cabeceras incorrectas. Revisa el contrato de columnas')
        rows=list(reader)
    if not rows or len(rows)>10000: raise ValueError('El archivo debe contener entre 1 y 10000 filas')
    if any(None in row or any(v is None for v in row.values()) for row in rows): raise ValueError('Fila con número incorrecto de columnas')
    return rows

def write_outputs(result,output):
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    (output/'proposal.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (output/'proposal.csv').open('w',newline='',encoding='utf-8-sig') as stream:
        fields=['item_no','description','location','supplier','status','need_qty','order_qty','amount','reason']
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader()
        for row in result['lines']: writer.writerow({k:safe_cell(row[k]) for k in fields})
    report=['# Circe · Propuesta de reposición','','DATOS FICTICIOS. Cálculo local. Ningún pedido creado.',
            f"Política: {result['policy_id']} v{result['policy_version']}. Umbral por línea: {result['review_threshold']} EUR.",'',
            '| Artículo | Almacén | Unidades | Importe EUR | Estado | Motivo |','|---|---|---:|---:|---|---|']
    for r in result['lines']: report.append('| '+' | '.join(md(r[k]) for k in ('item_no','location','order_qty','amount','status','reason'))+' |')
    report.extend(['',f"**Total de propuestas válidas: {result['total_proposed']} EUR.**",
                   f"{result['issue_lines']} incidencias excluidas. {result['special_review_lines']} líneas con revisión especial.",
                   'Toda propuesta requiere decisión humana. No incluye impuestos, transporte ni optimización entre almacenes.'])
    (output/'report.md').write_text('\n'.join(report)+'\n',encoding='utf-8')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True);parser.add_argument('--policy',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,required=True);args=parser.parse_args()
    try:
        result=calculate(load_rows(args.input),json.loads(args.policy.read_text(encoding='utf-8')))
        write_outputs(result,args.output_dir)
        print(json.dumps({k:v for k,v in result.items() if k!='lines'},ensure_ascii=False))
    except (ValueError,OSError,KeyError) as e: parser.exit(2,f'No se ha generado una propuesta válida: {e}\n')
if __name__=='__main__': main()
