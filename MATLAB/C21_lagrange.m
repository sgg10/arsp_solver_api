%Este programa halla el polinomio interpolante de los datos dados usando el
%m�todo de Lagrange

%Entradas: 
%X, abscisas 
%Y, ordenadas

%Salidas
%L, polinomios de Lagrange
%Coef, coeficientes del polinomio de interpolaci�n

%Creado por: Samir Posada
%�ltima actualizaci�n: 16/07/2020


function [L,Coef]=C21_lagrange(X,Y) 

file=fopen('lagrange.txt','w');

%Inicializaci�n
n=length(X);
L=zeros(n);

%Ciclo
for i=1:n   
    aux0=setdiff(X,X(i));
    aux=[1 -aux0(1)];
    for j=2:n-1
        aux=conv(aux,[1 -aux0(j)]);
    end
    L(i,:)=aux/polyval(aux,X(i));
end

fprintf(file,'\nL:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], L');

%Entrega de resultados
Coef=Y*L;

fprintf(file,'\nCoef:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], Coef');

% f = @(x) 0*x;
% for i = 1:n
%     f = @(x) f + Coef(n-i)*x^(n-i);
% end

end