import math
price=149.30; sh0=24.19; mcap=price*sh0
cash=53.5
fcf0=158.86-9.0-6.386
print(f"mcap={mcap:.1f} EV(sin deuda)={mcap-cash:.1f} FCF base={fcf0:.2f}")
def pv_growth(g,f0,r=0.09,gt=0.025,n=10):
    pv=0;f=f0
    for t in range(1,n+1):
        f*=1+g; pv+=f/(1+r)**t
    tv=f*(1+gt)/(r-gt); return pv+tv/(1+r)**n
lo,hi=-0.5,1
for _ in range(200):
    m=(lo+hi)/2
    if pv_growth(m,fcf0)>mcap: hi=m
    else: lo=m
print(f"g implícito (FCF accionista vs mcap) = {m*100:.2f}%")
lo,hi=-0.5,1
for _ in range(200):
    m2=(lo+hi)/2
    if pv_growth(m2,fcf0)>mcap-cash: hi=m2
    else: lo=m2
print(f"g implícito (vs EV sin deuda) = {m2*100:.2f}%")

R0=81.615+96.221+115.8+130.0
print(f"Ventas FY27e={R0:.1f}")
def path(y1,y5,y10,start=None):
    rev=[]
    if start is None:
        a=(y5/R0)**(1/5)
        for t in range(1,6): rev.append(R0*a**t)
    else:
        rev.append(start); a=(y5/start)**(1/4)
        for t in range(2,6): rev.append(start*a**(t-1))
    b=(y10/y5)**(1/5)
    for t in range(6,11): rev.append(y5*b**(t-5))
    return rev
def dcf(rev,m_tgt,m0=0.36,r=0.09,gt=0.025,verbose=False):
    pv=0;rows=[]
    for t,R in enumerate(rev,1):
        m=m0+(m_tgt-m0)*min(t,5)/5
        f=R*m; d=f/(1+r)**t; pv+=d; rows.append((t,R,m,f,d))
    tv=rev[-1]*m_tgt*(1+gt)/(r-gt); pvtv=tv/(1+r)**10
    return pv,tv,pvtv,rows
sc={'Pes':(380,450,.30,.40,60,24.5),'Base':(700,950,.40,.70,15,22.8),'Opt':(950,1400,.46,1.0,0,21.5)}
P={'Pes':.25,'Base':.50,'Opt':.25}
vals={}
for k,(y5,y10,m,inv,gl,sh) in sc.items():
    rev=path(None,y5,y10); pv,tv,pvtv,rows=dcf(rev,m)
    ev=pv+pvtv; eq=ev+cash+99*inv-gl; v=max(eq,0)/sh; vals[k]=v
    print(f"\n{k}: suma VP flujos={pv:.1f} TV={tv:.1f} VP TV={pvtv:.1f} EV={ev:.1f} +caja {cash} +inv {99*inv:.1f} -gar {gl} = Equity {eq:.1f} / {sh} = ${v:.2f}")
    for t,R,mm,f,d in rows: print(f"  A{t}: ventas {R:.0f} m {mm*100:.1f}% FCFF {f:.1f} VP {d:.1f}")
ev_=sum(P[k]*vals[k] for k in P); print(f"\nValor esperado = {ev_:.2f}")
print("\nSensibilidad base (r x g):")
y5,y10,m,inv,gl,sh=sc['Base']; rev=path(None,y5,y10)
for r in (.08,.09,.10):
    row=[]
    for g in (.02,.025,.03):
        pv,tv,pvtv,_=dcf(rev,m,r=r,gt=g); row.append((pv+pvtv+cash+99*inv-gl)/sh)
    print(r, ["%.0f"%x for x in row])
# alternativa: guia FY28 +75%
y1=R0*1.75; print(f"\nFY28 guia ~{y1:.0f}")
for k,(y5,y10,m,inv,gl,sh) in sc.items():
    rev=path(None,y5,y10,start=y1); pv,tv,pvtv,_=dcf(rev,m)
    print(f"Alt {k}: ${(max(pv+pvtv+cash+99*inv-gl,0))/sh:.2f}")
