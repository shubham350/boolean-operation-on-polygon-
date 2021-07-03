#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
#include <cmath>
using namespace std;

class Node {
  public:
  float data[2];
  Node* next;
};

float Area(float a[2],float b[2],float c[3])
{ 
  return abs((0.5*((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1]))));
}

void printlist(Node* tmp){
  if (tmp == NULL){
   cout << "list is empty";
  }
  else{
    while(tmp != NULL){
      cout << tmp-> data[0] << " ";
      cout << tmp-> data[1] << endl;
      tmp = tmp->next;
    }
  }
  cout << endl;
}

void insertatbeg(Node** head_ref, int a, int b){
  Node* new_node = new Node();
  new_node->data[0] = a;
  new_node->data[1] = b;
  new_node->next = *head_ref;
  *head_ref = new_node;
}   

float Area2(Node* head)
{
  float add = 0;
  Node* p = head;
  Node* a = p->next;
  while(a->next!=NULL)
  {
     add = add + Area(p->data, a->data, a->next->data);
     a = a->next;
  }
  return add;
} 

int main()
{
  string str;
  string myText;
  vector<string> v;
  vector<float> f;
  ifstream MyReadFile("input1.txt");
  
  while(getline(MyReadFile, myText))
  {
    str = myText;
    stringstream ss(str);
 
    while(ss.good())
    {
       string substr;
       getline(ss, substr,',');
       v.push_back(substr);
    }
  }

  for (size_t i = 0; i < v.size(); i++)
      f.push_back(stof(v[i]));

  for (auto i = f.begin(); i != f.end(); ++i)
        cout << *i << " ";
  
  cout << endl;

  //for( int j=0; j<f.size(); j++)
   //   cout << f[j]<< " ";

  Node* head = NULL;

  for(int j=0; j<f.size()/2;j++)
  {
     insertatbeg(&head,f[2*j],f[2*j+1]);
  }

  printlist(head); 
 
  cout << Area2(head);
   
  return 0;
}