#include <stdio.h>
#include <string.h>
void sort(int arr1[],char arr2[][100],int size);
void ort(int arr[],char arr2[][100],int size);
void max(int arr[],char arr2[][100],int size);
int main(void){
    char student[5][100];
    int not1[5];
    for(int i=0;i<5;i++){
        char name[100];
        int not;
        printf("enter the name and grade ? ");
        scanf("%s %d",name,&not);
        strcpy(student[i], name);
        not1[i]=not;
    }
    sort(not1,student,5);
    ort(not1,student,5);
    max(not1,student,5);
}
void sort(int arr1[],char arr2[][100],int size){
    for(int i=0;i<size;i++){
        for(int i2=0;i2<size-1;i2++){
            if(arr1[i2]>arr1[i2+1]){
                int c=arr1[i2];
                arr1[i2]=arr1[i2+1];
                arr1[i2+1]=c;

                char temp[100];
                strcpy(temp, arr2[i2]);
                strcpy(arr2[i2], arr2[i2+1]);
                strcpy(arr2[i2+1], temp);
            }
        }
    }
}
void ort(int arr1[],char arr2[][100],int size){
    int top=0;
    for(int i=0;i<size;i++){
        top+=arr1[i];
    }
    float ort=(float)top/(float)size;
    printf("Sinifin not ortalamasi: %.2f\n",ort);
}
void max(int arr1[],char arr2[][100],int size){
    sort(arr1,arr2,size);
    printf("En yuksek not: %d, Ogrenci: %s\n",arr1[size-1], arr2[size-1]);
}

    

