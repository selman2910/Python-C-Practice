#include <stdio.h>
int para=1000;
void paragörüntüle(){
    printf("para %d",para);
    return;
}
void parayatir(int *para,int para1){
    *para=(*para)+para1;
    return;
}
void paracek(int *para,int para1){
    if((*para)-para1<0){
        printf("no can do");
    }
    else{
        *para=(*para)-para1;
    }
    return;
}

int main(void){
    int y=1;
    while(y){
        printf("\n1 gör\n2 yatir\n3 cek\n4 cik\n");
        int x;
        printf("islem ? ");
        scanf("%d",&x);
        switch(x){
            case 1:
                paragörüntüle();
                break;
            case 2:
                int para1;
                printf("miktar ? ");
                scanf("%d",&para1);
                parayatir(&para,para1);
                break;
            case 3:
                int para2;
                printf("miktar ? ");
                scanf("%d",&para2);
                paracek(&para,para2);
                break;
            case 4:
                y=0;
                break;
            default:
                y=0;
                break;
        }
    }
    return 0;
}


