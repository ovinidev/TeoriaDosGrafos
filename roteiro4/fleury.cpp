#include<iostream>
#include<vector>
using namespace std;

class Graph{
	
	int vertex; // number of vertices
	vector<vector<int>> adj; // adjacency list
	
	public:
		
		// construtor para inicializar o gráfico
    // define o número de vértices para v
    // inicializa a lista de adjacência para v nós
		Graph(int v){
			vertex = v;
			adj = vector<vector<int>>(v+1);
		}
		
		// add edge (u, v) to graph
		void addEdge(int u, int v){
			adj[u].push_back(v);
			adj[v].push_back(u);
		}
		
		// remove edge (u, v) from the graph
		void removeEdge(int v,int u){
			
			// encontre o vértice u na lista de adjacência de v
      // troca u com o último vértice de adj [v]
      // deleta o último vértice
			for(int i=0;i<adj[v].size();++i){
				if(adj[v][i]==u){
					swap(adj[v][i], adj[v][adj[v].size()-1]);
					adj[v].pop_back();
					break;
				}
			}
			
      // encontre o vértice v na lista de adjacência de u
      // troca v com o último vértice de adj [u]
      // deleta o último vértice
			for(int i=0;i<adj[u].size();++i){
				if(adj[u][i]==v){
					swap(adj[u][i], adj[u][adj[u].size()-1]);
					adj[u].pop_back();
					break;
				}
			}
			
		}
		
      // função para imprimir o caminho do euler ou circuito do euler
      // a função primeiro verifica se o euler contém circuito euler ou caminho do euler
      // contando o número de vértices ímpares
		void printEulerPathCircuit(){
			
			int odd = 0; // número de vértices com grau ímpar
			int oddVertex = 0; // armazena vértice com grau ímpar se existir
			
			for(int i=1;i<=vertex;++i){
				if(adj[i].size()%2==1){
					++odd;
					oddVertex = i;
				}
			}
			
			if(odd==0){
        // se o número de vértices de grau ímpar for 0
        // o gráfico contém um circuito de Euler
        // podemos usar qualquer vértice como vértice inicial
				cout<<"Euler Circuit: ";
				// imprime o circuito de euler com '1' como vértice inicial
				printEuler(1);
			}
			else if(odd==2){
        // se o número de vértices de grau ímpar for 0
        // o gráfico contém um caminho de Euler
        // o vértice inicial deve ser de grau ímpar
				cout<<"Euler Path: ";
				printEuler(oddVertex);
			}
			else{
				cout<<"Euler Path/Circuit Doesn't Exist"<<endl;
			}
			
		}
		
		// a função para imprimir o caminho ou circuito do euler
		void printEuler(int v){
			
			// imprimir ponte atual
			cout<<" "<<v<<" ";
			
			// se não houver vértices adjacentes restantes
      // termina o programa
			if(adj[v].size()==0){
				return;
			}
			
      // se houver apenas 1 aresta conectada a v
      // escolha essa vantagem
			if(adj[v].size()==1){
				int u = adj[v][0];
				removeEdge(v, u);
				printEuler(u);
				return;
			}	
						
      // atravessa todos os vizinhos de v
      // para encontrar uma borda sem ponte
			for(auto u: adj[v]){

				if(isValidEdge(v, u)){
          // se a borda (v, u) não é uma ponte, é uma borda válida
          // então remova a borda (v, u) e defina u como a borda atual
					removeEdge(v, u);
					printEuler(u);
					return;
				}
				
			}
			
		}
		
		// esta função verifica se (v, u) é uma ponte ou não
		bool isValidEdge(int v, int u){
			
			int c1, c2;
			c1 = c2 = 0;
			vector<bool> visited;
			
			// primeiro removemos a borda (v, u) do gráfico
      // então conte o número de vértices que podemos alcançar a partir de v
			removeEdge(v, u);
			visited = vector<bool>(vertex+1,false);
			c1 = countConnectedVertices(u, visited);
			
			// adicionamos o vértice (v, u) de volta ao gráfico
      // então conte o número de vértices que podemos alcançar a partir de v
			addEdge(v, u);
			visited = vector<bool>(vertex+1,false);
			c2 = countConnectedVertices(u, visited);
			
      // se c1 == c2, isso significa que o vértice (v, u) não é uma ponte
      // remover (v, u) não desconecta o gráfico
      // se c1! = c2, isso significa que o vértice (v, u) é uma ponte
      // remover (v, u) desconecta o gráfico
			if(c2 == c1) return true;
			else		 return false;
			
		}
		
		// profundidade primeira pesquisa para contar o número de vértices
    // podemos alcançar de você
		int countConnectedVertices(int u, vector<bool> &visited){
			
			visited[u] = true;
			int count = 1;
			for(auto v: adj[u]){
				if(!visited[v]){
					count += countConnectedVertices(v, visited);
				}
			}
			return count;
			
		}
	
};

int main()
{
	// gráfico G, contendo 7 vértices de 1 a 7.
	Graph G(7);
	
  // adicionando bordas ao gráfico
  // este gráfico é igual ao gráfico que usamos no exemplo acima
  // a-1 b-2 c-3 d-4 e-5 f-6 g-7
  // estamos assumindo que o gráfico está conectado e não direcionado
	G.addEdge(1,2);
	G.addEdge(1,3);
	G.addEdge(1,4);
	G.addEdge(1,6);
	G.addEdge(2,3);
	G.addEdge(2,5);
	G.addEdge(2,7);
	G.addEdge(5,6);
	G.addEdge(6,7);
	
	// função para imprimir o caminho de Euler ou circuito de Euler
	G.printEulerPathCircuit();
}