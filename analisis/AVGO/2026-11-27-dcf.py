# AVGO DCF encadenado (contrato 2026-11-27-tesis.md)
price=300.86; sh0=4.888; cash=24.0; debt=66.1
mcap=price*sh0
fcf0=7.67+8.01+10.262+13.7-8.4   # OCF Q4FY25 aprox (capex Q4FY25 omitido) + FCF Q1-Q3 FY26 - SBC anualizado (9M x 4/3)
print(f"mcap={mcap:.1f}  FCF base (post SBC)={fcf0:.2f}")
def pvg(g,f0,r=.09,gt=.025):
    pv=0;f=f0
    for t in range(1,11): f*=1+g; pv+=f/(1+r)**t
    return pv+f*(1+gt)/(r-gt)/(1+r)**10
lo,hi=-.5,1
for _ in range(200):
    m=(lo+hi)/2
    if pvg(m,fcf0)>mcap: hi=m
    else: lo=m
print(f"g implícito FCF accionista vs mcap = {m*100:.2f}%")
R0=19.311+22.187+29.6+34.8
print(f"FY26e ventas={R0:.1f}")
sc={'Pes':(150,170,.28,35,5.1,.25),'Base':(260,340,.36,8,4.9,.50),'Opt':(350,480,.40,0,4.75,.25)}
def run(k,r=.09,g=.025,v=False,m0=.39):
    y5,y10,mt,extra,sh,p=sc[k]; a=(y5/R0)**.2; b=(y10/y5)**.2
    rev=[R0*a**t for t in range(1,6)]+[y5*b**t for t in range(1,6)]
    f=[R*(m0+(mt-m0)*min(t,5)/5) for t,R in enumerate(rev,1)]
    pv=sum(x/(1+r)**t for t,x in enumerate(f,1)); tv=rev[-1]*mt*(1+g)/(r-g); pvtv=tv/(1+r)**10
    ev=pv+pvtv; eq=ev+cash-debt-extra; val=max(eq,0)/sh
    if v:
        print(f"\n{k}: VP flujos {pv:.1f}; VT {tv:.1f}; VP VT {pvtv:.1f}; EV {ev:.1f}; +caja {cash} -deuda {debt} -extra {extra} = Equity {eq:.1f} / {sh} = ${val:.2f}")
        for t,(R,x) in enumerate(zip(rev,f),1): print(f"  A{t}: ventas {R:.1f} FCFF {x:.1f} VP {x/(1+r)**t:.1f}")
    return val
vals={k:run(k,v=True) for k in sc}
print(f"\nValor esperado = {sum(sc[k][5]*vals[k] for k in sc):.2f}")
print("Sensibilidad base:")
for r in (.08,.09,.10): print(r,["%.2f"%run('Base',r,g) for g in (.02,.025,.03)])
# Alternativa: Año 1 anclado a guía FY27 (IA $115B + software y semis no-IA ≈ $45B ≈ $160B)
def alt(k,y1=160.0,r=.09,g=.025,m0=.39):
    y5,y10,mt,extra,sh,p=sc[k]; a=(y5/y1)**.25; b=(y10/y5)**.2
    rev=[y1*a**t for t in range(0,5)]+[y5*b**t for t in range(1,6)]
    f=[R*(m0+(mt-m0)*min(t,5)/5) for t,R in enumerate(rev,1)]
    pv=sum(x/(1+r)**t for t,x in enumerate(f,1)); pvtv=rev[-1]*mt*(1+g)/(r-g)/(1+r)**10
    return max(pv+pvtv+cash-debt-extra,0)/sh
print("Alt (A1=160):",{k:round(alt(k),2) for k in sc})
