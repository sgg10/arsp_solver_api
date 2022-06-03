%Este programa halla la soluci�n al sistema Ax=b usando el m�todo de Jacobi

%Entradas: 
%A, matrix invertible
%b, vector constante
%x0, aproximaci�n inicial 
%tol, tolerancia
%Nmax, n�mero m�ximo de iteraciones

%Salidas
%x, soluci�n
%iter, n�mero de iteraciones
%err, error

%Creado por: Samir Posada
%�ltima actualizaci�n: 16/07/2020

function [x,iter,err]=C16_jacobi(A,b,x0,tol,Nmax)

file=fopen('jacobi.txt','w')

if det(A) == 0
    disp("Error: Det(A) = 0");
    fprintf(fileID,'%s\r\n',"Error: Det(A) = 0");
    x = NaN;
    iter = NaN;
    err = NaN;
    return
end

%Inicializaci�n
D=diag(diag(A));
L=-tril(A)+D;
U=-triu(A)+D;
T=inv(D)*(L+U);
C=inv(D)*b;
xant=x0;
E=1000;
cont=0;
n=size(A,1);
n1=size(T,1);
n2=size(C,1);
specratio = max(abs(eig(T)));
norm2 = norm(A);

fprintf(file,'\nD:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], D');
fprintf(file,'\nL:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], L');
fprintf(file,'\nU:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], U');
fprintf(file,'\nT:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], T');
fprintf(file,'\nC:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], C');
fprintf(file,'\n');

fprintf(file,'\nSpectral Radio (T):');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], specratio);
fprintf(file,'\n');

fprintf(file,'\nEuclidean Norm (A):');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], norm2);
fprintf(file,'\n');

if specratio >= 1
    fprintf(file,'\nWARNING: Spectral Radio is equal or higher than 1.');
    fprintf(file,'\nMethod stopped.');
    return
end

fprintf(file,'x(%u):', cont+1);
fprintf(file,[repmat(' %.6f ',1,n) '\n'], xant');
fprintf(file,'\n');

%Ciclo
while E>tol && cont<Nmax 
    xact=T*xant+C
    E=norm(xant-xact)
    xant=xact
    cont=cont+1
    fprintf(file,'x(%u):', cont+1);
    fprintf(file,[repmat(' %.6f ',1,n) '\n'], xant');
    fprintf(file,'\n');
end

%Entrega de resultados
x=xact;
iter=cont;
err=E;

fprintf(file,'\nx:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], x');
fprintf(file,'\nError:\n');
fprintf(file,[repmat(' %.2i ',1,n) '\n'], err);
fprintf(file,'\n');
end