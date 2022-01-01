#include <stdio.h>

main()
{
	FILE *fp;
	fp=fopen("b.txt","r+");
	char buffer[8],c,cc;
	fread(buffer,8,1,fp);
	rewind(fp);
	for(c=0;c<=7;c++)
	{
		*(buffer + c) = ~ *(buffer+c);/*-1/3+25*/
	}
	fwrite(buffer,8,1,fp);
	fflush(fp);
	close(fp);
}
