#include <stdio.h>
#include <string.h>
#define TSIZE 45/*存储片名的数组大小*/
#define FMAX  5 /*影片的最大数量*/

struct film
{
    /* data */
    char title[TSIZE];
    int rating;
};
char * s_get(char * st,int n);
char * s_get(char * st,int n)
{
    char * ret_val;
    char * find;
    ret_val = fgets(st,n,stdin);
    if(ret_val)
    {
        find = strchr(st,'\n');
        if(find)
        {
            *find = '\0';
        }
        else
        {
            while (getchar()!='\n')
            {
                /* code */
                continue;
            }
            
        } 
    }
    return ret_val;
}

int main(void)
{
    struct film movies[FMAX];
    int i = 0;
    int j;
    puts("Enter first movie titie:");
    while (i < FMAX && s_get(movies[i].title,TSIZE)!=NULL && movies[i].title[0] != '\0')
    {
        /* code */
       puts("enter your rating <0~10>");
       scanf("%d",&movies[i++].rating);
       while (getchar() != '\n')
       {
           /* code */
           continue;
       }
       puts("enter next movies title(empty line to stop)");
    }
    if(i == 0)
    {
        printf("no data enter");
    }
    else
    {
        printf("here is the movies list:\n");
    }
    for(j = 0;j < i;j++)
    {
        printf("movies:%s\trating:%d\n",movies[j].title,movies[j].rating);
    }
    printf("bye");
    return 0;
}
