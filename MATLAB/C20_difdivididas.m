%Este programa halla el polinomio interpolante de los datos dados usando el
%m�todo de diferencias divididas

%Entradas: 
%X, abscisas 
%Y, ordenadas

%Salidas
%Coef, coeficientes del polinomio de Newton

%Creado por: Samir Posada
%�ltima actualizaci�n: 16/07/2020

function [Coef,M]=C20_difdivididas(X,Y)

file=fopen('difdiv.txt','w')

%Inicializaci�n
n=length(X);
D=zeros(n);

%Ciclo
D(:,1)=Y';
for i=2:n
    aux0=D(i-1:n,i-1);
    aux=diff(aux0);
    aux2=X(i:n)-X(1:n-i+1);
    D(i:n,i)=aux./aux2';

end

fprintf(file,'\nD:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], D');

%Entrega de resultados
M = D;
Coef=diag(D)';

fprintf(file,'\nCoef:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], Coef');
end