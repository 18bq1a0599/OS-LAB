#include<stdio.h>
int main(){
 int p,a[10],i,temp,n=0;
 char ch='y';
 printf("\nEnter the size of physical memory for user processes:");
 scanf("%d",&p);
 temp=p;
 for(i=0;ch=='y';i++,n++)
 {
   printf("\nEnter memory required for process%d:",i+1);
   scanf("%d",&a[i]);
   if(a[i]<=temp)
   {
     printf("\nMemory is allocated for Process%d:",i+1);
     temp = temp - a[i];
   }
   else
   {
     printf("\nMemory is Full");
     break;
   }
   printf("\nDo you want to continue(y/n) -- ");
   scanf(" %c",&ch);
 }
 printf("\n\nTotal Memory Available:%d",p);
 printf("\n\n\tPROCESS\t\t MEMORY ALLOCATED FOR PROCESSES ");
 for(i=0;i<n;i++)
  printf("\n \t%d\t\t%d",i+1,a[i]);
 printf("\n\nTotal Memory Allocated is:%d",p-temp);
 printf("\nExternal Fragmentation :%d",temp);
 return 0;
}
