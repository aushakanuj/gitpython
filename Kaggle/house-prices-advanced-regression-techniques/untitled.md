#define INFINITY 9999 
#include<iostream> 
#include<stdio.h> 
#include<string.h> 
#include<stdlib.h> 
    using namespace std; 
    #define MAX 100
    void push(); 
    void delet();
    typedef struct node
    {
        struct node *next; int vertex,weight;
    }node;
    string name[100];
    node *G[10];//adjacency list int n;// Number of vertices void readgraph();
    void insert(int,int,int); void dijkstra(int);
    void djkstra(int,int); void push();
    int compare(string,string); void del();
int main()
{
string u; readgraph(); int ch=0;
int i; while(ch!=5)
{
cout<<"Options	\n"; cout<<"1- print distance form one
vertex to all others\n"; cout<<"2-vertices in a given radius\n"; cout<<"3-insert a vertex\n";
cout<<"4-delete a vertice\n"; cout<<"5-exit\n";
cout<<" 	\n"; cin>>ch;
int t; switch(ch)
{
case 1:cout<<"\nEnter the starting node : "; cin>>u;

 
for(i=0;i<n;i++)
{
if(name[i].compare(u)==0)

break;
}
dijkstra(i); break;
case 2:cout<<"\nEnter the starting node : "; cin>>u;
for(i=0;i<n;i++)
{
if(name[i].compare(u)==0) break;
}
cout<<"\nEnter the radius"; int r;
cin>>r; djkstra(i,r); break;
case 3:push(); break;
case 4: del(); break;
case 5: break;
default: cout<<"Invalid input";
}
}
}
void dijkstra(int startnode)
{
int distance[MAX],pred[MAX];
int visited[MAX],count,mindistance,nextnode = 0,i,j; node *p;
for(i=0;i<n;i++)
{
distance[i]=INFINITY; pred[i]=startnode;visited[i]=0;
}
distance[startnode]=0; count=0; while(count<n-1)
{
mindistance=INFINITY ; for(i=0;i<n;i++)
if(distance[i] < mindistance && !visited[i])
{
 
mindistance=distance[i]; nextnode=i;
}
visited[nextnode]=1; for(p=G[nextnode];p!=NULL;p=p->next) if(!visited[p->vertex])
if(mindistance+p->weight<distance[p->vertex])
{
distance[p->vertex]=mindistance+p->weight; pred[p->vertex]=nextnode;
}
count++;
}
for(i=0;i<n;i++)
{
if(i!=startnode)
{
cout<<"\n Distance of "<< i<<" = "<<distance[i]; cout<<" Path = "<<i; j=i; do
{
j=pred[j]; cout<<"<- "<<j;
}while(j!=startnode);
}
}
}
int adj[100][100]; void readgraph()
{
int i,j;
cout<<"\nEnter no. of vertices :"; cin>>n;
cout<<"Enter the names of the cities"; for(i=0;i<n;i++)
{
cin>>name[i];
}
cout<<"\nEnter Adjacency matrix :\n"; for(i=0;i<n;i++)
for(j=0;j<n;j++) cin>>adj[i][j]; for(i=0;i<n;i++) G[i]=NULL;
for(i=0;i<n;i++) for(j=0;j<n;j++) if(adj[i][j]!=0)
insert(i,j,adj[i][j]);
 
}
void insert(int vi,int vj,int w)
{

node *p,*q;
q=(node *)malloc(sizeof(node)); q->vertex=vj;
q->next=NULL; q->weight=w; if(G[vi]==NULL)
G[vi]=q; else
{
p=G[vi];
while(p->next!=NULL) p=p->next;
p-	>next=q;
}
}
void djkstra(int startnode,int radius)
{
int distance[MAX],pred[MAX];
int visited[MAX],count,mindistance,nextnode = 0,i,j; node *p;
for(i=0;i<n;i++)
{
distance[i]=INFINITY; pred[i]=startnode;visited[i]=0;
}
distance[startnode]=0; count=0; while(count<n-1)
{
mindistance=INFINITY ; for(i=0;i<n;i++)
if(distance[i] < mindistance && !visited[i])
{
mindistance=distance[i]; nextnode=i;
}
visited[nextnode]=1; for(p=G[nextnode];p!=NULL;p=p->next) if(!visited[p->vertex])
if(mindistance+p->weight<distance[p->vertex])
{
distance[p->vertex]=mindistance+p->weight; pred[p->vertex]=nextnode;
 
}
count++;
}

for(i=0;i<n;i++)
{
if(i!=startnode && distance[i]<=radius)
{
cout<<"\n Distance of "<<i<<" = "<<distance[i]; cout<<" Path = "<<name[i]; j=i; do
{
j=pred[j]; cout<<"<- "<<j;
}while(j!=startnode);
}
}
}
void push()
{
n=n+1;
cout<<"Enter the distance from other vertices to the new vertex in order"; int i;
for(i=0;i<n-1;i++)
{
cin>>adj[i][n-1];
}
cout<<"1-directed graph, 2- undirected graph"; int ch;
cin>>ch; if(ch==1)
{
for(i=0;i<n-1;i++)
{
cin>>adj[n-1][i];
}
}
else if(ch==2)
{
for(i=0;i<n-1;i++)
{
adj[i][n-1]=adj[n-1][i];
}
}
}
void del()
{
int t=-1;
 
string city;
cout<<"Enter the name of the city you would like to remove from the graph"; cin>>city;
int i; for(i=0;i<n;i++)
{
if(name[i]==city)
{
t=i; name[i]=""; break;
}
}
if(t>-1)
{
for(i=0;i<n;i++)
{ adj[t][i]=INFINITY; adj[i][t]=INFINITY;
}
}
else
cout<<"City not found";
}