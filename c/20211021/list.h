#ifndef LIST_H_
#define LIST_H_
#include <stdbool.h>

/*如果编译器不支持bool*/
// enum bool
// {
//     false,
//     true
// }


/*特殊类型声明*/
#define TSIZE 45
struct film
{
    /* data */
    char title[TSIZE];
    int rating;
};


/*一般类型声明*/
typedef struct film Item;

typedef struct node
{
    Item item;
    struct node * next;
}Node;

typedef Node * List;

/*函数原型*/
/*操作：        初始化一个链表*/
/*参数          plist指向一个链表*/
/*返回值        链表初始化为空*/
void InitializeList(List * plist);

/*操作：        确定链表为空时，plist指向一个已初始化的链表*/
/*返回值        如果链表为空，该函数返回true;否则返回false*/
bool ListIsEmpty(const List * plist);

/*操作：        确定链表已满时，plist指向一个已初始化的链表*/
/*返回值        如果链表已满，该函数返回true;否则返回false*/
bool ListIsFull(const List * plist);

/*操作：        确定链表中的项数，plist指向一个初始化的链表*/
/*返回值        该函数返回链表中的项数*/
unsigned int ListItemCount(const List * plist);

/*操作：        在链表的末尾添加项*/
/*参数          item是一个待添加链表的项，plist指向一个已经初始化的链表*/
/*返回值        添加成功返回true,否则返回false*/
bool AddItem(Item item,List * plist);

/*操作：        函数作用于链表中的每一项*/
/*参数          plist指向一个已经初始化的链表，pfun指向一个函数，函数接受一个Item类型的参数，而且无返回值*/
void Traverse(const List * plist,void (* pfun)(Item Item));

/*操作：        清空函数，释放内存*/
/*参数          plist指向一个已经初始化的链表*/
void EmptyTheList(List * plist);

#endif