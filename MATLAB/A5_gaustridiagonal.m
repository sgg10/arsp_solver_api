%Este programa halla la solución al sistema Ax=b usando el método de
%eliminación gaussiana tridiagonal. 

%Entradas: 
%A, matrix invertible
%b, vector constante

%Salidas
%x, solución

%Creado por: Pascual Gómez
%Última actualización: 04/04/2022

function [x,M] = A5_gaustridiagonal(A,b) 

%Inicialización
N=size(A,1);
M=[A b];

d = b;
a = diag(A,-1);
b = diag(A);
c = diag(A,1);

c(1) = c(1) / b(1);
d(1) = d(1) / b(1); 

fileID = fopen('sol_gausstri.txt','wt'); % Crea un archivo .txt
fprintf(fileID,'%s\r\n',"Matriz inicial"); % Genera la primera línea
fprintf(fileID,'%s\r\n',"---------------");
%NOTA: \r\n sirve como salto de línea para archivos .txt de windows.

for ii = 1:length(M(:,1))
    fprintf(fileID,'%.5f %.7d %g\t',M(ii,:)); % Imprime cada fila de la matriz
    fprintf(fileID,'\n'); % Genera un salto de línea
end

for n = 2:1:N-1
    temp = b(n) - a(n) * c(n - 1);
    if (n<N)
        c(n) = c(n) / temp;
    end
    d(n) = (d(n) - a(n) * d(n - 1)) / temp;
end
 
x(N) = d(N);
for n = (N - 1):-1:1
    x(n) = d(n) - c(n) * x(n + 1);
end

fprintf(fileID,'%s\r\n',"---------------");
fprintf(fileID,'%s\r\n',"Solución");
fprintf(fileID,'%s\r\n',"---------------");
for ii = 1:length(x(:,1))
    fprintf(fileID,'%.5f %.7d %g \t',x(ii,:)); % Imprime cada fila de la matriz
    fprintf(fileID,'\n'); % Genera un salto de línea
end

fclose(fileID);

end