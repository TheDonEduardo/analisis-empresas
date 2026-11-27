# META DCF encadenado (contrato 2026-11-27-tesis.md). $B
price=609.89; sh0=2.573; cash=82.45; pref_cash=12.5; fwd_cash=25.0; debt=80.9
mcap=price*sh0; print(f"mcap={mcap:.1f}")
# DCF inverso sobre FCF 2025 ($43,59B, antes de SBC: SBC no disponible)
def pvg(g,f0,r=.09,gt=.025):
    pv=0;f=f0
    for t in range(1,11): f*=1+g; pv+=f/(1+r)**t
    return pv+f*(1+gt)/(r-gt)/(1+r)**10
lo,hi=-.5,1
for _ in range(200):
    m=(lo+hi)/2
    if pvg(m,43.59)>mcap: hi=m
    else: lo=m
print(f"g implícito sobre FCF 2025 (43,59) vs mcap = {m*100:.2f}%")
R0=249.0  # 2026e aprox
sc={'Pes':(330,400,[-25,-15],.15,35+10,2.75,.25),'Base':(430,600,[-10],.22,15,2.65,.50),'Opt':(520,800,[],.28,5,2.55,.25)}
def run(k,r=.09,g=.025,v=False):
    y5,y10,burn,mt,adj,sh,p=sc[k]; a=(y5/R0)**.2; b=(y10/y5)**.2
    rev=[R0*a**t for t in range(1,6)]+[y5*b**t for t in range(1,6)]
    nb=len(burn); f=[]
    for t in range(10):
        if t<nb: f.append(burn[t])
        elif t<5:
            m0=0.05 if nb==0 else 0.0
            f.append(rev[t]*(m0+(mt-m0)*(t-nb+1)/(5-nb)))
        else: f.append(rev[t]*mt)
    pv=sum(x/(1+r)**(t+1) for t,x in enumerate(f)); tv=rev[-1]*mt*(1+g)/(r-g); pvtv=tv/(1+r)**10
    ev=pv+pvtv; eq=ev+cash+pref_cash+fwd_cash-debt-adj; val=max(eq,0)/sh
    if v:
        print(f"\n{k}: VP flujos {pv:.1f}; VT {tv:.1f}; VP VT {pvtv:.1f}; EV {ev:.1f}; +caja {cash}+pref {pref_cash}+plazo {fwd_cash} -deuda {debt} -ajustes {adj} = Equity {eq:.1f} / {sh} = ${val:.2f}")
        for t,(R,x) in enumerate(zip(rev,f),1): print(f"  A{t}: ventas {R:.1f} FCFF {x:.1f} VP {x/(1+r)**t:.1f}")
    return val
vals={k:run(k,v=True) for k in sc}
print(f"\nValor esperado = {sum(sc[k][6]*vals[k] for k in sc):.2f}")
print("Sensibilidad base:")
for r in (.08,.09,.10): print(r,["%.2f"%run('Base',r,g) for g in (.02,.025,.03)])
