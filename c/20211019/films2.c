/*使用结构链表*/
#include <stdio.h>
#include <stdlib.h>//提供malloc 原型
#include <string.h>//提供strcpy原型
#define TSIZE 45

struct film
{
    /* data */
    char title[TSIZE];
    int  rating;
    struct film * next;//指向链表的下一个结构
};
char * s_get(char * st,int n);
int main(void)
{
    struct film * head = NULL;
    struct film *prev,*current;
    char input[TSIZE];

    /*收集并存储信息*/
    puts("enter first movies title:");
    while(s_get(input,TSIZE) != NULL && input[0] != '\0')
    {
        current = (struct film *)malloc(sizeof(struct film));
        if(head == NULL)
        {
            head = current;
        }
        else
        {
            prev->next = current;
        }
        current->next = NULL;
        strcpy(current->title,input);
        puts("enter your rating 0~10");
        scanf("%d",&current->rating);
        while (getchar() != '\n')
        {
            /* code */
            continue;
        }
        puts("enter next movies title");
        prev = current;
    }

    /*显示电影列表*/
    if(head = NULL)
    {
        printf("no data");
    }
    else
    {
        printf("here is movie list");
    }
    current = head;
    while(current != NULL)
    {
        printf("title:%s\trating:%d",current->title,current->rating);
        current = current->next;
    }

    /*完成任务，释放内存*/
    current = head;
    while(current != NULL)
    {
        head = current->next;
        free(current);
        current = current->next;
    }
    printf("bye");
    return 0;
}
char * s_get(char * st,int n)
{
    char * ret_val;
    char * find;

    ret_val = fgets(st,n,stdin);
    if(ret_val)
    {
        find = strchr(st,'\n');//查找换行符
        if(find)//如果地址不是NULL
        {
            *find = '\0';//在此处放置一个空字符
        }
        else
        {
            while(getchar() != '\n')
            {
                continue;//处理剩余行
            }
        }
    }
    return ret_val;
}