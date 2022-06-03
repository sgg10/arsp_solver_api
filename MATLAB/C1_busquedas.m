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
    count = i;
end

T = array2table(tbl, 'VariableNames',{'i' 'a' 'b' 'f(a)' 'f(b)'});
T.(2) = num2str(T.(2), '%.6f%');
T.(3) = num2str(T.(3), '%.6f%');
T.(4) = num2str(T.(4), '%.6f%');
T.(5) = num2str(T.(5), '%.6f%');

% T.Style = [T.Style 
%     {NumberFormat("%.6f"),...
%     Width("100%"),...
%     Border("solid"),...
%     ColSep("solid"),...
%     RowSep("solid")}];
% T.TableEntriesHAlign = "center";

if Nmax==count && xant*xact >= 0
    disp("***************************************************************************")
    disp("WARNING: Method failed on finding an interval.")
    disp("***************************************************************************")
end
disp(T);

%Entrega de resultados
a=xant;
b=xact;
iter=i;
end