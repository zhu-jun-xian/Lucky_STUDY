#include <stdio.h>
#include <stdlib.h>
#include "list.h"

/*局部函数原型*/
static void CopyToNode(Item item,Node * pnode);

/*接口函数*/
void InitializeList(List * plist)
{
    plist = NULL;
}

/*如果链表为空，返回true*/
bool ListIsEmpty(const List * plist)
{
    if(&plist == NULL)
        return 1;
    else 
        return 0;
}

/*如果链表已满，返回true*/
bool ListIsFull(const List * plist)
{
    Node * pt;
    bool full;

    pt = (Node *)malloc(sizeof(Node));
    if(pt == NULL)
    {
        full  = true;
    }
    else 
    {
        full = false;
    }
    free(pt);
    return full;
}

/*返回节点的数量*/
unsigned int ListItemCount(const List * plist)
{
    unsigned int count  = 0;
    Node * pnode = *plist;

    while (pnode != NULL)
    {
        /* code */
        ++count;
        pnode = pnode->next;
    }
    return count;
}

/*创建存储项的节点，并将其添加到由plist指向的链表末尾*/
bool AddItem(Item item,List * plist)
{
    Node * pnew;
    Node * scan = *plist;
    pnew = (Node *)malloc(sizeof(Node));
    if(pnew == NULL)
    {
        return false;
    }
    CopyToNode(item,pnew);
    pnew->next = NULL;
    if(scan == NULL)
    {
        *plist = pnew;
    }
    else
    {
        while (scan->next != NULL)
        {
            /* code */
            scan = scan->next;
        }
        scan->next = pnew;
    }
    return true;
}

/*访问每个节点并执行pfun指向的函数*/
void Traverse(const List * plist,void(* pfun)(Item item))
{
    Node * pnode = *plist;
    while (pnode != NULL)
    {
        /* code */
        (*pfun)(pnode->item);
        pnode = pnode->next;
    }
}

/*释放由malloc分配的内存*/
/*设置链表的指针为NULL*/
void EmptyTheList(List * plist)
{
    Node * psave;
    while(*plist != NULL)
    {
        psave = (*plist)->next;
        free(*plist);
        *plist = psave;
    }
}

/*局部函数定义*/
/*把一个项拷贝到节点中*/
static void CopyToNode(Item item,Node * pnode)
{
    pnode->item = item;
}