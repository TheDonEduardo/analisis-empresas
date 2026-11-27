# CRDO DCF encadenado (contrato 2026-11-27-tesis.md). $M
price=106.80; sh0=188.0; cash=1400.0
mcap=price*sh0; print(f"mcap={mcap:.0f}")
def pvg(g,f0,r=.09,gt=.025):
    pv=0;f=f0
    for t in range(1,11): f*=1+g; pv+=f/(1+r)**t
    return pv+f*(1+gt)/(r-gt)/(1+r)**10
lo,hi=-.5,1
for _ in range(200):
    m=(lo+hi)/2
    if pvg(m,472.3)>mcap: hi=m
    else: lo=m
print(f"g implícito (proxy: beneficio neto FY26 $472,3M; FCF no disponible) = {m*100:.2f}%")
R0=2500.0; m0=0.25   # margen FCFF inicial: supuesto propio (beneficio neto FY26 = 35 % de ventas, menos SBC/capex)
sc={'Pes':(2500,3000,.15,205,.30),'Base':(5500,9000,.25,198,.45),'Opt':(8000,14000,.30,195,.25)}
def run(k,r=.09,g=.025,v=False):
    y5,y10,mt,sh,p=sc[k]; a=(y5/R0)**.2; b=(y10/y5)**.2
    rev=[R0*a**t for t in range(1,6)]+[y5*b**t for t in range(1,6)]
    f=[R*(m0+(mt-m0)*min(t,5)/5) for t,R in enumerate(rev,1)]
    pv=sum(x/(1+r)**t for t,x in enumerate(f,1)); tv=rev[-1]*mt*(1+g)/(r-g); pvtv=tv/(1+r)**10
    ev=pv+pvtv; eq=ev+cash; val=eq/sh
    if v:
        print(f"\n{k}: VP flujos {pv:.0f}; VT {tv:.0f}; VP VT {pvtv:.0f}; EV {ev:.0f}; +caja {cash} = Equity {eq:.0f} / {sh}M = ${val:.2f}")
        for t,(R,x) in enumerate(zip(rev,f),1): print(f"  A{t}: ventas {R:.0f} FCFF {x:.0f} VP {x/(1+r)**t:.0f}")
    return val
vals={k:run(k,v=True) for k in sc}
print(f"\nValor esperado = {sum(sc[k][4]*vals[k] for k in sc):.2f}")
print("Sensibilidad base:")
for r in (.08,.09,.10): print(r,["%.2f"%run('Base',r,g) for g in (.02,.025,.03)])
