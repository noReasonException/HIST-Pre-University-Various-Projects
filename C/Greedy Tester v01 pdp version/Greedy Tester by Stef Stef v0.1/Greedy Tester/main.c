#include <stdio.h>
#include <stdlib.h>


int main()
{
    system("@echo off");
    system("color e");
    int counter,result,errors=0;
    char name[30];
    char command[30]="copy test0.in share.in >nul";
    int solvearray[8]={13,15,178,5665,16662914,55467,36,16662868};
    printf("Greedy Tester by stef stef v0.1\n");
    printf("PDP version\n");
    printf("Executable name[or full path] > ");
    scanf("%s",&name);
    system("color a");
    for(counter=0;counter<8;counter++,command[9]++){
        printf("test%d > ",counter);
        FILE *in,*out;


        system(command);
        system(name);
        out=fopen("share.out","r");
        fscanf(out,"%d",&result);


        if(solvearray[counter]==result){

            printf("ok\n",counter);

        }
        else{

            printf("Invalid Return Value (%d != %d} \n",solvearray[counter],result);
            errors+=1;
            system("color c");

        }





    }

    printf("===================================================\n");
    printf("Test Completed\n");
    printf("Error(s) = %d\n",errors);
    printf("Success rate = %d / 8\n",8-errors);
    printf("press enter to exit()");
    scanf("\n",&counter);

}
