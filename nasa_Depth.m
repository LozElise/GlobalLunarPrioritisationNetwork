clear all
clc
inputT=readtable('Terrain_Cooridnates.csv');
inpT=table2array(inputT);
T=zeros();
X=zeros();
Y=zeros();
for i=1:1:100
    for j=1:1:100
        T(i,j)=inpT(i,j);
        Tx(i,j)=inpT(i,j);
        X(i,j)=j;
        Y(i,j)=i;
        if(T(i,j)<120)
            T(i,j)=0;
        elseif (T(i,j)>142)
            T(i,j)= 0;
        end
        
        if (T(i,j)<=127 && T(i,j)>=120)
            T(i,j) = T(i,j)-127;
        elseif (T(i,j)<=142&&T(i,j)>=127)
            T(i,j) = T(i,j)-127;
        end
            
    end
end
Ts=zeros();
sum=0;
k=1;l=1;
sum=0;
for m=1:1:10
    m1=m*10;
    sum=0;temp1=0;temp=0;x=1;y=1;
    for n=1:1:10
        n1=n*10;
        sum=0;temp1=0;temp=0;
        for i=x:1:m1
            for j=y:1:n1
                temp=T(i,j);
                temp1=abs(temp);
                sum=sum+temp1;
            end
        end
        x=x+10;
        y=y+10;
        Ts(m,n)=sum;
        X1(m,n)=n;
        Y1(m,n)=m;
    end
end
% figure 01 - Terrain of Moon,as per M3 camera data from Chandrayana-1
figure
surf(X,Y,Tx)

% figure 02 - Terrain of Moon,Available site within the Limit -100m to 1000m 
hold on
figure
surf(X,Y,T)

% figure 03 - Terrain of Moon,Landing Site Detection 
hold on
figure
surf(X1,Y1,Ts)

