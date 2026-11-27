# ORCL DCF encadenado (contrato 2026-11-27-tesis.md)
price=108.68; sh0=3.09; cash=31.9; debt=135.0; pref=5.0
R0=90.0
sc={ # y5,y10, burn por año (Y1..), rampa de margen tras equilibrio, margen objetivo, ajuste extra, acciones, prob
 'Pes':(110,120,[-50,-45,-35,-20],[0.08],0.08,20,3.8,.35),
 'Base':(200,260,[-45,-35],[0.06,0.12,0.18],0.18,0,3.4,.45),
 'Opt':(260,380,[-45],[0.10,0.17,0.22,0.25],0.25,0,3.15,.20)}
def path(y5,y10):
    a=(y5/R0)**(1/5); b=(y10/y5)**(1/5)
    return [R0*a**t for t in range(1,6)]+[y5*b**t for t in range(1,6)]
def run(k,r=0.09,g=0.025,verbose=False):
    y5,y10,burn,ramp,mt,extra,sh,p=sc[k]; rev=path(y5,y10); f=[]
    for t in range(10):
        if t<len(burn): f.append(burn[t])
        elif t-len(burn)<len(ramp): f.append(rev[t]*ramp[t-len(burn)])
        else: f.append(rev[t]*mt)
    pv=sum(x/(1+r)**(t+1) for t,x in enumerate(f))
    tv=rev[-1]*mt*(1+g)/(r-g); pvtv=tv/(1+r)**10; ev=pv+pvtv
    eq=ev+cash-debt-pref-extra; v=max(eq,0)/sh
    if verbose:
        print(f"\n{k}: burn total {sum(burn)}; VP flujos {pv:.1f}; VT {tv:.1f}; VP VT {pvtv:.1f}; EV {ev:.1f}; +caja {cash} -deuda {debt} -pref {pref} -extra {extra} = Equity {eq:.1f} / {sh} = ${v:.2f}")
        for t,(R,x) in enumerate(zip(rev,f),1): print(f"  A{t}: ventas {R:.1f} FCFF {x:.1f} VP {x/(1+r)**t:.1f}")
    return v
vals={k:run(k,verbose=True) for k in sc}
ve=sum(sc[k][7]*vals[k] for k in sc); print(f"\nValor esperado = {ve:.2f}")
print("mcap",round(price*sh0,1),"EV",round(price*sh0+debt+pref-cash,1))
print("Sensibilidad base:")
for r in (.08,.09,.10): print(r,["%.2f"%run('Base',r,g) for g in (.02,.025,.03)])
print("Base a WACC 10%:",round(run('Base',.10),2),"Pes 10%:",round(run('Pes',.10),2),"Opt 10%:",round(run('Opt',.10),2))
