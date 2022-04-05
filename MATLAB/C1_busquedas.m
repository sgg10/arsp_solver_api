%Este programa encuentra un intervalo donde f(x) tiene cambio de signo
%usando el método de búsquedas incrementales

%Entradas: 
%f, función continua
%x0, punto inicial
%h, paso
%Nmax, número máximo de iteraciones

%Salidas
%a, extremo izquierdo del intervalo
%b, extremo derecho del intervalo
%iter, número de iteraciones

%Creado por: Samir Posada
%última actualización: 16/07/2020


function [a,b,iter]=C1_busquedas(f,x0,h,Nmax)

%Inicialización
xant=x0; 
fant=f(xant);
xact=xant+h; 
fact=f(xact);

tbl = [];

%Ciclo
for i=1:Nmax
    tbl = [tbl;i,xant,xact,fant,fact];
    if fant*fact<0
        break;
    end
    xant=xact;
    fant=fact;
    xact=xant+h;
    fact=f(xact);
end

T = array2table(tbl, 'VariableNames',{'i' 'a' 'b' 'f(a)' 'f(b)'});

disp(T);

%Entrega de resultados
a=xant;
b=xact;
iter=i;
end