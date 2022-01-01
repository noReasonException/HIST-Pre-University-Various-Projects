#include <stdio.h>
void main()
{
	int copy,counter,counter02,len;
	scanf("%d",&len);
	int [10]={
	for(counter=0;counter<=len-1;counter++){
		for(counter02=len-1;counter02<=counter;counter--){
			if (array[counter02] < array[counter02 - 1]) {
				copy=array[counter];
				array[counter] = array[counter +1];
				array[counter +1] = copy;
			}
				
		}
	}
}
