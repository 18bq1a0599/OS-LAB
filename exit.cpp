#include <sys/types.h>
#include <sys/wait.h>
int main(void)  
{  
   pid_t pid = fork();  
   if ( pid == 0 )  
   {  
      exit(9999); //passing value more than 255  
   }  
   int status;  
   waitpid(pid, &status, 0);  
   if ( WIFEXITED(status) )  
   {  
       int exit_status = WEXITSTATUS(status);
       printf("Exit code: %d\n", exit_status);  
   }  
return 0;  
}