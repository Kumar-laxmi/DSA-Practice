#include<iostream>
using namespace std;

class Node
{
    public:
        int data;
        Node *next;
        Node()
        {
            next = NULL;
        }
};
class LinkedList
{
    Node *head;
    public:
        LinkedList()
        {
            head = NULL;
        }
        void InsertInBeginning(int newValue);
        void InsertInEnd(int newValue);
        void InsertNode(int newValue,int position);

        void UpdateNode(int newValue,int position);

        void DeleteInBeginning();
        void DeleteInEnd();
        void DeleteNode(int position);

        int Length();

        void PrintList();
};
void LinkedList::InsertInBeginning(int newValue)
{
    Node *newNode = new Node();
    newNode->data = newValue;
    newNode->next = head;
    head = newNode;
    cout<<"<<<"<<newValue<<" inserted successfully at beginning of list>>>"<<endl;
}
void LinkedList::InsertInEnd(int newValue)
{
    Node *newNode = new Node();
    newNode->data = newValue;

    // If the list is not empty
    Node *ptr = new Node();
    ptr = head;

    // To transverse to the end of the List
    while(ptr!=NULL)
    {
        ptr = ptr->next;
    }
    ptr->next = newNode;
    cout<<"<<<"<<newValue<<" inserted successfully at end of list>>>"<<endl;
}
void LinkedList::InsertNode(int newValue,int position)
{
    if(head==NULL)
    {
        // If the list is empty
        cout<<"List is empty so placing "<<newValue<<" as head node"<<endl;
        Node *newNode = new Node();
        newNode->data = newValue;

        head = newNode;
    }
    else if(position<0 || position>=Length())
    {
        cout<<"Invalid position specified, Position out of bound"<<endl;
    }
    else if(position==0)
    {
        InsertInBeginning(newValue);
    }
    else if(position==Length()-1)
    {
        InsertInEnd(newValue);
    }
    else
    {
        Node *newNode = new Node();
        newNode->data = newValue;

        int counter = 0; // To count the current position reached while transversing

        Node *ptr = new Node();
        ptr = head;

        while(ptr!=NULL)
        {
            if(counter==position)
            {
                newNode->next = ptr->next;
                ptr->next = newNode;
                break;
            }
            counter++;
            ptr = ptr->next;
        }
        cout<<"<<<"<<newValue<<" inserted successfully at position "<<position<<" of list>>>"<<endl;
    }
}
void LinkedList::UpdateNode(int newValue,int position)
{
    if(head==NULL)
    {
        cout<<"Sorry List is Empty!!! ==> Invalid Updation request"<<endl;
    }
    else
    {
        Node *ptr = new Node();
        ptr = head;

        int counter = 0;   // To keep track of position transversed

        while(ptr!=NULL)
        {
            if(counter==position)
            {
                ptr->data = newValue;
                break;
            }
            counter++;
            ptr = ptr->next;
        }
    }
}
void LinkedList::DeleteInBeginning()
{
    Node *temp = new Node();
    temp = head;
    head = head->next;

    cout<<temp->data<<" deleted at beginning of the list successfully"<<endl;
    free(temp);
}
void LinkedList::DeleteInEnd()
{
    Node *ptr = new Node();
    Node *temp = new Node();

    while(ptr->next!=NULL)
    {
        ptr = ptr->next;
    }
    temp = ptr->next;
    ptr->next = NULL;

    cout<<temp->data<<" deleted at end of the list successfully"<<endl;
    free(temp);
}
void LinkedList::DeleteNode(int position)
{
    if(head==NULL)
    {
        cout<<"List is empty!!! ==> Invalid Deletion request"<<endl;
    }
    else if(position<0 || position>=Length())
    {
        cout<<"Invalid position specified, Position out of bound"<<endl;
    }
    else if(position==0)
    {
        DeleteInBeginning();
    }
    else if(position==Length()-1)
    {
        DeleteInEnd();
    }
    else
    {
        Node *ptr = new Node();
        Node *temp = new Node();
        ptr = head;

        int counter = 0;  //To keep track of position transversed

        while(ptr!=NULL)
        {
            if(counter==position-1)
            {
                temp = ptr->next;
                ptr->next = temp->next;
                cout<<"Element "<<temp->data<<" deleted at position "<<position<<endl;
                free(temp);
            }
            ptr = ptr->next;
            counter++;
        }
    }
}
int LinkedList::Length()
{
    Node *ptr = new Node();
    ptr = head;
    
    int length = 0;
    while(ptr!=NULL)
    {
        length++;
        ptr = ptr->next;
    }
    
    return length;
}
void LinkedList::PrintList()
{
    if(head==NULL)
    {
        cout<<"List is Empty"<<endl;
    }
    else
    {
        Node *ptr = new Node();
        ptr = head;
        while(ptr!=NULL)
        {
            cout<<"->"<<ptr->data;
            ptr = ptr->next;
        }
        cout<<endl;
    }
}
int main()
{
    LinkedList ll;
    int choice,newData,position;
    cout<<"Enter 1 to Insert node"<<endl;
    cout<<"Enter 2 to Update node"<<endl;
    cout<<"Enter 3 to Delete node"<<endl;
    cout<<"Enter 4 to Print the length of node"<<endl;
    cout<<"Enter 5 to Print Linked List"<<endl;
    cout<<"Enter 6 to exit"<<endl;

    while(true)
    {
        cout<<"\nEnter your choice: ";
        cin>>choice;

        if(choice==1)
        {
            cout<<"Enter the data: ";
            cin>>newData;
            cout<<"Enter the position: ";
            cin>>position;
            ll.InsertNode(newData,position);
        }
        else if(choice==2)
        {
            cout<<"Enter the data: ";
            cin>>newData;
            cout<<"Enter the position: ";
            cin>>position;
            ll.UpdateNode(newData,position);
        }
        else if(choice==3)
        {
            cout<<"Enter the position: ";
            cin>>position;
            ll.DeleteNode(position);
        }
        else if(choice==4)
        {
            cout<<"The length of List is: "<<ll.Length()<<" nodes"<<endl;
        }
        else if(choice==5)
        {
            cout<<"THE LIST IS ==>"<<endl;
            ll.PrintList();
        }
        else if(choice==6)
        {
            cout<<"\n\t\tThank you!!\n";
            break;
        }
        else
        {
            cout<<"Sorry invalid choice entered!!, Enter the value again :)"<<endl;
        }
    } 
    
    return 0;
}
