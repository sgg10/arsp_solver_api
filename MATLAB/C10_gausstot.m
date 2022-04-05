%Este programa halla la soluci�n al sistema Ax=b usando el m�todo de
%eliminaci�n gaussiana con pivoteo total. 

%Entradas: 
%A, matrix invertible
%b, vector constante

%Salidas
%x, soluci�n

%Creado por: Samir Posada
%�ltima actualizaci�n: 16/07/2020

function [x,M]=C10_gausstot(A,b) 

%Inicializaci�n
n=size(A,1);
M=[A b];
cambi=[];

fileID = fopen('sol_gausstot.txt','wt'); % Crea un archivo .txt
fprintf(fileID,'%s\r\n',"Matriz inicial"); % Genera la primera línea
fprintf(fileID,'%s\r\n',"---------------");
%NOTA: \r\n sirve como salto de línea para archivos .txt de windows.

for ii = 1:length(M(:,1))
    fprintf(fileID,'%.5f %.7d %g\t',M(ii,:)); % Imprime cada fila de la matriz
    fprintf(fileID,'\n'); % Genera un salto de línea
end

%Reducimos el sistema
for i=1:n-1
    [a,b]=find(abs(M(i:n,i:n))==max(max(abs(M(i:n,i:n)))));
    %Cambio de columna
    if b(1)+i-1~=i
        cambi=[cambi; i b(1)+i-1];
        aux2=M(:,b(1)+i-1);
        M(:,b(1)+i-1)=M(:,i);
        M(:,i)=aux2;
    end   
    %Cambio de filas
    if a(1)+i-1~=i
        aux2=M(i+a(1)-1,i:n+1);
        M(a(1)+i-1,i:n+1)=M(i,i:n+1);
        M(i,i:n+1)=aux2;
    end
    for j=i+1:n
        if M(j,i)~=0
           M(j,i:n+1)=M(j,i:n+1)-(M(j,i)/M(i,i))*M(i,i:n+1);
        end
    end

    fprintf(fileID,'%s\r\n',"---------------");
    fprintf(fileID,'%s\r\n',"Etapa " + i); % Imprime el número de la etapa
    fprintf(fileID,'%s\r\n',"---------------");
    for ii = 1:length(M(:,1))
    fprintf(fileID,'%.5f %.7d %g \t',M(ii,:)); % Imprime cada fila de la matriz
    fprintf(fileID,'\n'); % Genera un salto de línea
    end
end

%Entrega de resultados
x=sustregr(M); %Sustituci�n regresiva
%reordenamos el vector soluci�n
for i=size(cambi,1):-1:1
    aux=x(cambi(i,1));
    x(cambi(i,1))=x(cambi(i,2));
    x(cambi(i,2))=aux;
end

fprintf(fileID,'%s\r\n',"---------------");
fprintf(fileID,'%s\r\n',"Solución"); % Imprime el número de la etapa
fprintf(fileID,'%s\r\n',"---------------");
for ii = 1:length(x(:,1))
fprintf(fileID,'%.5f %.7d %g \t',x(ii,:)); % Imprime cada fila de la matriz
fprintf(fileID,'\n'); % Genera un salto de línea
end

fclose(fileID);

end