#include<stdio.h>
int main(){
 int fragment[10],c[20],p[20],i,j,nb,np,temp,least=9999,flag[10],allocate[10],mp,high=0,temp1;
 int barray[20],parray[20],bar[20],par[20];
 printf("Enter size of physical memory for user processes:");
 scanf("%d",&mp);
 printf("\nEnter number of partitions:");
 scanf("%d",&nb);
 printf("\nEnter number of processes:");
 scanf("%d",&np);
 printf("\nEnter size of partitions:-\n");
 for(i=1;i<=nb;i++){
    printf("Block no. %d:",i);
    scanf("%d",&c[i]);
 }
 printf("\nEnter size of processes:-\n");
 for(i=1;i<=np;i++){
    printf("Process no. %d:",i);
    scanf("%d",&p[i]);
 }
 printf("\nBEST FIT");
 for(i=1;i<=np;i++)
{
for(j=1;j<=nb;j++)
{
if(barray[j]!=1)
{
temp=c[j]-p[i];
if(temp>=0)
if(least>temp)
{
parray[i]=j;
least=temp;
}
}

}
fragment[i]=least;
        barray[parray[i]]=1;
        least=10000;
}
printf("\nProcess-No\tProcess-Size\tBlock-No\tBlock-Size\tInternal-Fragmentation");
for(i=1;i<=np && parray[i]!=0;i++)
printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d",i,p[i],parray[i],c[parray[i]],fragment[i]);
    for(i = 0; i < 10; i++)
{
flag[i] = 0;
allocate[i] = -1;
}
for(i = 1; i <= np; i++)
for(j = 1; j <= nb; j++)
if(flag[j] == 0 && c[j] >= p[i])
{
allocate[j] = i;
flag[j] = 1;
break;
}
    printf("\n\nFIRST FIT");
printf("\nBlock-No\t\tBlock-Size\t\tProcess-No\t\tProcess-Size\t\tInternal-Fragmentation");
for(i = 1; i <=nb; i++)
{
printf("\n%d\t\t\t%d\t\t\t",i,c[i]);
if(flag[i] == 1)
printf("%d\t\t\t%d\t\t\t%d",allocate[i]+1,p[allocate[i]],c[i]-p[allocate[i]]);
else
printf("Not allocated");
}
printf("\n\nWORST FIT");
    for(i=1;i<=np;i++)
{
for(j=1;j<=nb;j++)
{
if(bar[j]!=1)
{
temp1=c[j]-p[i];
if(temp1>=0)
if(high<temp1)
{
par[i]=j;
high=temp1;
}
}

}
fragment[i]=high;
        bar[par[i]]=1;
        high=0;
}
printf("\nProcess-No\tProcess-Size\tBlock-No\tBlock-Size\tInternal-Fragmentation");
for(i=1;i<=np && par[i]!=0;i++)
       printf("\n%d\t\t%d\t\t%d\t\t%d\t\t\%d",i,p[i],par[i],c[par[i]],fragment[i]);
return 0;
}
