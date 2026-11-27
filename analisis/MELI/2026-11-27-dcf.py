# MELI DCF encadenado (contrato 2026-11-27-tesis.md). $M
price=1532.0; sh0=51.0; netdebt=8030.0
mcap=price*sh0; print(f"mcap={mcap:.0f}")
def pvg(g,f0,r=.09,gt=.025):
    pv=0;f=f0
    for t in range(1,11): f*=1+g; pv+=f/(1+r)**t
    return pv+f*(1+gt)/(r-gt)/(1+r)**10
lo,hi=-.5,1
for _ in range(200):
    m=(lo+hi)/2
    if pvg(m,2000)>mcap: hi=m
    else: lo=m
print(f"g implícito (proxy: beneficio neto 2025 $2.000M; FCF no disponible) = {m*100:.2f}%")
R0=40000.0; m0=0.04  # margen FCFF inicial: supuesto propio (FCF absorbido por el crecimiento del crédito)
sc={'Pes':(65000,85000,.05,2000,51.5,.25),'Base':(90000,150000,.09,0,50.5,.50),'Opt':(110000,200000,.12,0,49.5,.25)}
def run(k,r=.09,g=.025,v=False):
    y5,y10,mt,extra,sh,p=sc[k]; a=(y5/R0)**.2; b=(y10/y5)**.2
    rev=[R0*a**t for t in range(1,6)]+[y5*b**t for t in range(1,6)]
    f=[R*(m0+(mt-m0)*min(t,5)/5) for t,R in enumerate(rev,1)]
    pv=sum(x/(1+r)**t for t,x in enumerate(f,1)); tv=rev[-1]*mt*(1+g)/(r-g); pvtv=tv/(1+r)**10
    ev=pv+pvtv; eq=ev-netdebt-extra; val=max(eq,0)/sh
    if v:
        print(f"\n{k}: VP flujos {pv:.0f}; VT {tv:.0f}; VP VT {pvtv:.0f}; EV {ev:.0f}; -deuda neta {netdebt} -extra {extra} = Equity {eq:.0f} / {sh}M = ${val:.2f}")
        for t,(R,x) in enumerate(zip(rev,f),1): print(f"  A{t}: ventas {R:.0f} FCFF {x:.0f} VP {x/(1+r)**t:.0f}")
    return val
vals={k:run(k,v=True) for k in sc}
print(f"\nValor esperado = {sum(sc[k][5]*vals[k] for k in sc):.2f}")
print("Sensibilidad base:")
for r in (.08,.09,.10): print(r,["%.2f"%run('Base',r,g) for g in (.02,.025,.03)])
