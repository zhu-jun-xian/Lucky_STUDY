/*使用抽象数据类型（ADT）*/
/*第一步：建立接口*/
/*第二步：使用接口*/
/*第三步：实现接口*/

//官方库引用使用<>,私有库使用""
#include <stdio.h>
#include <stdlib.h>
#include "list.h"
#include <string.h>

void showmovie(Item item);

char * s_gets(char * st,int n);
int main(void)
{
    List movies;
    Item temp;

    /*初始化*/
    InitializeList(&movies);
    if(ListIsFull(&movies))
    {
        fprintf(stderr,"链表已满！\n");
        exit(1);
    }

    /*获取用户输入并存储*/
    puts("enter first movies title:");
    while (s_gets(temp.title,TSIZE) != NULL && temp.title[0] != '\0')
    {
        /* code */
        puts("enter your rating <0-10>");
        scanf("%d",&temp.rating);
        while (getchar() != '\n')
        {
            /* code */
            continue;
        }
        if(AddItem(temp,&movies) == false)
        {
            fprintf(stderr,"内存分配失败\n");
            break;
        }
        if(ListIsFull(&movies))
        {
            puts("The list is now full\n");
            break;
        }
        puts("enter next movies\n");
    }

    /*显示*/
    if(ListIsEmpty(&movies))
        printf("no data enter");
    else
    {
        printf("here is the movie list:\n");
        Traverse(&movies,showmovie);
    }
    printf("you enter %d movies.\n",ListItemCount(&movies));

    /*清理*/
    EmptyTheList(&movies);
    printf("bye\n");
    return 0;
    
}
void showmovie(Item item)
{
    printf("Movies:%s\tRating:%d\n",item.title,item.rating);
}
char * s_gets(char * st,int n)
{
    char * ret_val;
    char * find;
    ret_val = fgets(st,n,stdin);
    if(ret_val)
    {
        find = strchr(st,'\n');
        if(find)
            *find = '\0';
        else
            while (getchar() != '\n')
            {
                /* code */
                continue;
            }
            
    }
    return ret_val;
}