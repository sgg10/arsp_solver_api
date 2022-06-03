%Este programa halla el polinomio interpolante de los datos dados usando el
%m�todo de Vandermonde

%Entradas: 
%X, abscisas 
%Y, ordenadas

%Salidas
%Coef, coeficientes del polinomio

%Creado por: Samir Posada
%�ltima actualizaci�n: 16/07/2020

function [Coef,A,M]=C19_vandermonde(X,Y)
    
file=fopen('vander.txt','w')

%Inicializaci�n
n=length(X);
A=zeros(n);
M = [];

%Ciclo
for i=1:n
    A(:,i)=(X.^(n-i))';
end

fprintf(file,'\nA:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], A');

%Entrega de resultados
Coef=A\Y';
%[Coef,M]=C8_gausspl(A,Y');
%[Coef,M]=C9_gausspar(A,Y');
%[Coef,M]=C10_gausstot(A,Y');

fprintf(file,'\nCoef:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n\n'], Coef');

count = 1;
for i=length(Coef):-1:1
    fprintf(file,'%u',Coef(count));
    fprintf(file,'*x^%u',i-1);
    if i-1 > 0
        fprintf(file,' + ');
    end
    count = count + 1;
end

end