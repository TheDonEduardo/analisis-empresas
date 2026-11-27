"""Indicadores técnicos (EMA21, SMA50/150/200, ATR14, RSI14, volumen, rango 52s) a partir de un JSON con listas close/high/low/volume (barras diarias de IBKR). Uso: python scripts/tecnico.py barras.json"""
import json,sys
d=json.load(open(sys.argv[1])); C,H,L,V=d['close'],d['high'],d['low'],d['volume']
n=len(C); assert n==len(H)==len(L)==len(V)
p=C[-1]; sma=lambda k,off=0:sum(C[n-k-off:n-off])/k
e=C[0];a=2/22
for c in C[1:]: e=c*a+e*(1-a)
tr=[max(H[i]-L[i],abs(H[i]-C[i-1]),abs(L[i]-C[i-1])) for i in range(1,n)]
atr=sum(tr[:14])/14
for t in tr[14:]: atr=(atr*13+t)/14
g=[max(C[i]-C[i-1],0) for i in range(1,n)]; l=[max(C[i-1]-C[i],0) for i in range(1,n)]
ag=sum(g[:14])/14; al=sum(l[:14])/14
for i in range(14,len(g)): ag=(ag*13+g[i])/14; al=(al*13+l[i])/14
print("n",n,"price",p)
for nm,v in [("EMA21",e),("SMA50",sma(50)),("SMA150",sma(150)),("SMA200",sma(200))]: print(nm,round(v,2),f"{(p/v-1)*100:.1f}%")
print("SMA50 hace20",round(sma(50,20),2),"SMA150 hace20",round(sma(150,20),2),"SMA200 hace20",round(sma(200,20),2))
print("ATR14",round(atr,2),f"{atr/p*100:.1f}%","RSI14",round(100-100/(1+ag/al),1))
print("Vol5",round(sum(V[-5:])/5/1e6,1),"M media50",round(sum(V[-50:])/50/1e6,1),"M")
print("52w max",max(H),"min",min(L),f"caida {(p/max(H)-1)*100:.1f}%")
print("ult15 C",C[-15:]); print("ult15 L",L[-15:]); print("ult15 H",H[-15:])
