# RKLB DCF encadenado (contrato 2026-11-27-tesis.md). $M
price=47.02; sh0=639.2
bridge=4704-3150-1700   # caja+valores - efectivo Iridium - deuda neta Iridium
R0=1000.0
sc={'Pes':(2000,3000,[-375]*4,[],0.05,300,850,.40),
    'Base':(3500,7000,[-400,-400],[0.05,0.10],0.15,0,760,.40),
    'Opt':(5000,11000,[-500],[0.08,0.13,0.18],0.22,0,720,.20)}
def run(k,r=.09,g=.025,v=False):
    y5,y10,burn,ramp,mt,extra,sh,p=sc[k]; a=(y5/R0)**.2; b=(y10/y5)**.2
    rev=[R0*a**t for t in range(1,6)]+[y5*b**t for t in range(1,6)]; f=[]
    for t in range(10):
        if t<len(burn): f.append(burn[t])
        elif t-len(burn)<len(ramp): f.append(rev[t]*ramp[t-len(burn)])
        else: f.append(rev[t]*mt)
    pv=sum(x/(1+r)**(t+1) for t,x in enumerate(f)); tv=rev[-1]*mt*(1+g)/(r-g); pvtv=tv/(1+r)**10
    ev=pv+pvtv; eq=ev+bridge-extra; val=max(eq,0)/sh
    if v:
        print(f"\n{k}: VP flujos {pv:.0f}; VT {tv:.0f}; VP VT {pvtv:.0f}; EV {ev:.0f}; puente {bridge} -extra {extra} = Equity {eq:.0f} / {sh}M = ${val:.2f}")
        for t,(R,x) in enumerate(zip(rev,f),1): print(f"  A{t}: ventas {R:.0f} FCFF {x:.0f} VP {x/(1+r)**t:.0f}")
    return val
vals={k:run(k,v=True) for k in sc}
print(f"\nValor esperado = {sum(sc[k][7]*vals[k] for k in sc):.2f}")
print("mcap",round(price*sh0),"puente",bridge)
print("Sensibilidad base:")
for r in (.08,.09,.10): print(r,["%.2f"%run('Base',r,g) for g in (.02,.025,.03)])
print("Con 11%:",{k:round(run(k,.11),2) for k in sc})
