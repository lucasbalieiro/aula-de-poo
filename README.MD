# Programação Orientada a Objetos (POO) - Python

Este é um breve guia sobre Programação Orientada a Objetos (POO) em Python. Vamos explorar os principais conceitos da POO e fornecer exemplos práticos em Python para ilustrar cada um deles.

## O que é Programação Orientada a Objetos?

A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em torno de objetos, que são instâncias de classes. Em vez de se concentrar em funções e procedimentos, a POO se concentra em modelar entidades do mundo real como objetos, que têm atributos (dados) e métodos (comportamentos). Isso ajuda a criar um código mais modular, reutilizável e fácil de entender.

## Principais Conceitos da POO

### 1. Classe

Uma classe é um modelo ou plano para criar objetos. Ela define os atributos e métodos que um objeto pode ter. Em Python, uma classe é definida usando a palavra-chave `class`. Aqui está um exemplo simples:

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def ligar(self):
        print("O carro está ligado.")
```

### 2. Objeto

Um objeto é uma instância de uma classe. Ele representa uma entidade específica com seus próprios valores de atributos e comportamentos. Você pode criar um objeto usando a classe como um "molde". Veja um exemplo:

```python
meu_carro = Carro("Ford", "Fiesta")
```

### 3. Atributo

Um atributo é uma variável associada a um objeto. Ele armazena dados que pertencem a esse objeto específico. Os atributos são acessados usando a notação de ponto (`objeto.atributo`). Veja um exemplo:

```python
print(meu_carro.marca)  # Output: Ford
```

### 4. Método

Um método é uma função associada a um objeto. Ele define o comportamento do objeto e pode acessar e manipular seus atributos. Os métodos são chamados usando a notação de ponto (`objeto.metodo()`). Veja um exemplo:

```python
meu_carro.ligar()  # Output: O carro está ligado.
```

### 5. Encapsulamento

O encapsulamento é o princípio de ocultar os detalhes internos de um objeto e fornecer uma interface externa para interagir com ele. Em Python, isso é alcançado usando modificadores de acesso como `_` (atributos/métodos protegidos) e `__` (atributos/métodos privados). Veja um exemplo:

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo protegido
    
    def __saudacao(self):
        print(f"Olá, meu nome é {self._nome}")  # Método privado

p = Pessoa("Alice")
print(p._nome)  # Output: Alice
p.__saudacao()  # Erro: AttributeError
```

### 6. Herança

A herança permite criar uma nova classe baseada em uma classe existente, herdando seus atributos e métodos. A classe derivada (filha) pode adicionar novos atributos/métodos ou substituir os existentes. Isso promove a reutilização de código e a criação de hierarquias de classes. Veja um exemplo:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

c = Cachorro("Rex")
c.emitir_som()  # Output: Au au!
```

### 7. Polimorfismo

O polimorfismo permite que objetos de diferentes classes sejam tratados de maneira semelhante, chamando os mesmos métodos. Isso é possível porque as classes compartilham uma superclasse em comum ou uma interface comum. Veja um exemplo:

```python
def fazer_som(animal):
    animal.emitir_som()

c = Cachorro("Rex")
fazer_som(c)  # Output: Au au!
```

## Conclusão

Este guia forneceu uma introdução aos principais conceitos da Programação Orientada a Objetos (POO) em Python. Lembre-se de que a POO é uma abordagem poderosa para escrever código modular e reutilizável, que ajuda a modelar entidades do mundo real de forma mais intuitiva. Experimente criar suas próprias classes e objetos para explorar ainda mais a POO em Python!