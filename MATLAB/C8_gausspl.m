%Este programa halla la solución al sistema Ax=b usando el método de
%eliminación gaussiana simple. 

%Entradas: 
%A, matrix invertible
%b, vector constante

%Salidas
%x, solución

%Creado por: Samir Posada
%Última actualización: 16/07/2020

function [x,M] = C8_gausspl(A,b) 

%Inicialización
n=size(A,1);
M=[A b];


fileID = fopen('sol_gauss.txt','wt'); % Crea un archivo .txt
fprintf(fileID,'%s\r\n',"Matriz inicial"); % Genera la primera línea
fprintf(fileID,'%s\r\n',"---------------");
%NOTA: \r\n sirve como salto de línea para archivos .txt de windows.

for ii = 1:length(M(:,1))
    fprintf(fileID,'%.5f %.7d %g\t',M(ii,:)); % Imprime cada fila de la matriz
    fprintf(fileID,'\n'); % Genera un salto de línea
end



%Reducimos el sistema
for i=1:n-1
    for j=i+1:n
        if M(j,i)~=0
           M(j,i:n+1)=M(j,i:n+1)-(M(j,i)/M(i,i))*M(i,i:n+1);
        else
            fprintf(fileID,'%s\r\n',"---------------");
            fprintf(fileID,'%s\r\n',"ERROR: La diagonal tiene un cero."); % Imprime el número de la etapa
            fprintf(fileID,'%s\r\n',"---------------");
        end
    end

    fprintf(fileID,'%s\r\n',"---------------");
    fprintf(fileID,'%s\r\n',"Etapa " + i); % Imprime el número de la etapa
    fprintf(fileID,'%s\r\n',"---------------");
    for ii = 1:length(M(:,1))
    fprintf(fileID,'%.5f %.7d %g\t',M(ii,:)); % Imprime cada fila de la matriz
    fprintf(fileID,'\n'); % Genera un salto de línea
    end

end

%Entrega de resultados
x=sustregr(M); %Sustitución regresiva

fprintf(fileID,'%s\r\n',"---------------");
fprintf(fileID,'%s\r\n',"Solución"); % Imprime el número de la etapa
fprintf(fileID,'%s\r\n',"---------------");
for ii = 1:length(x(:,1))
fprintf(fileID,'%.5f %.7d %g \t',x(ii,:)); % Imprime cada fila de la matriz
fprintf(fileID,'\n'); % Genera un salto de línea
end

fclose(fileID);

end