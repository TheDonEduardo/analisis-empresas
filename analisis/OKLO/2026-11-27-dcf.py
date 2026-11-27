# OKLO DCF encadenado (contrato 2026-11-27-tesis.md). Importes en $M.
price=20.50; sh0=195.29; cash=3131.0   # excluye $81,9M restringidos; sin deuda material
# escenario: ventas A5, A10, quema por año (A1..), rampa de margen tras la quema, margen objetivo, acciones, prob
sc={'Pes':(0,50,[-350]*10,[],-0.20,320,.50),
    'Base':(150,1500,[-500]*5,[0.05,0.10],0.15,250,.35),
    'Opt':(600,4000,[-500]*4,[0.10,0.15,0.20],0.25,225,.15)}
def path(y5,y10):
    early=[y5*t/5 for t in range(1,6)]           # rampa lineal hasta A5
    if y5==0: return early+[y10*t/5 for t in range(1,6)]
    b=(y10/y5)**.2; return early+[y5*b**t for t in range(1,6)]
def run(k,r=.09,g=.025,v=False):
    y5,y10,burn,ramp,mt,sh,p=sc[k]; rev=path(y5,y10); f=[]
    for t in range(10):
        if t<len(burn): f.append(burn[t])
        elif t-len(burn)<len(ramp): f.append(rev[t]*ramp[t-len(burn)])
        else: f.append(rev[t]*mt)
    pv=sum(x/(1+r)**(t+1) for t,x in enumerate(f))
    tv=max(rev[-1]*mt*(1+g)/(r-g),0) if mt>0 else 0.0   # sin valor terminal si el margen es negativo
    pvtv=tv/(1+r)**10; ev=pv+pvtv; eq=ev+cash; val=max(eq,0)/sh
    if v:
        print(f"\n{k}: quema total {sum(burn)}; VP flujos {pv:.1f}; VT {tv:.1f}; VP VT {pvtv:.1f}; EV {ev:.1f}; +caja {cash} = Equity {eq:.1f} / {sh}M = ${val:.2f}")
        for t,(R,x) in enumerate(zip(rev,f),1): print(f"  A{t}: ventas {R:.0f} FCFF {x:.0f} VP {x/(1+r)**t:.1f}")
    return val
vals={k:run(k,v=True) for k in sc}
print(f"\nValor esperado = {sum(sc[k][6]*vals[k] for k in sc):.2f}")
print("mcap",round(price*sh0,1),"EV",round(price*sh0-cash,1),"caja/accion",round(cash/sh0,2))
print("Sensibilidad base:")
for r in (.08,.09,.10): print(r,["%.2f"%run('Base',r,g) for g in (.02,.025,.03)])
print("Con tasa 12%:",{k:round(run(k,.12),2) for k in sc}, "VE", round(sum(sc[k][6]*run(k,.12) for k in sc),2))
