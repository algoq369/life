# Life: Conceptual Intelligence System

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-alpha-orange.svg)]()

> Building genuine intelligence through concepts, relationships, and human-like reasoning—not neural networks or gradient descent.

**Life** is a conceptual intelligence system that learns concepts, ideologies, and philosophies through natural teaching rather than massive datasets. It represents knowledge as visual networks, implements metacognition for reflective reasoning, and analyzes situations from multiple ideological perspectives.

## 🎯 Philosophy

We believe the future of AI isn't more complex math—it's more intuitive design. Life implements:

- **Visual Knowledge Graphs**: Concepts connected by meaningful relationships
- **Metacognition Space**: A "thinking space" where AI reflects before responding
- **Ideological Reasoning**: Multiple perspectives encoded as value hierarchies
- **Transparent Reasoning**: Every decision is explainable and traceable
- **Human-Like Learning**: Teaching through examples and conversation, not backpropagation

## ⚡ Quick Start

```bash
# Install
pip install -e .

# Run demo
python examples/demo.py
```

You'll see:
- A visual knowledge graph generated as an image
- Real-time reasoning through concept relationships
- Multi-perspective ideological analysis
- Complete transparency into the thinking process

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│   METACOGNITION LAYER                   │
│   System 1 (fast) + System 2 (slow)     │
└─────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│   CONCEPT GRAPH LAYER                   │
│   Visual network of interconnected      │
│   concepts and relationships            │
└─────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│   IDEOLOGY LAYER                        │
│   Value hierarchies + reasoning         │
│   principles for multiple perspectives  │
└─────────────────────────────────────────┘
```

## 📚 Core Components

### Concept Graph
Store knowledge as visual networks where concepts are nodes and relationships are edges.

```python
from life import ConceptGraph

kb = ConceptGraph()
kb.add_concept("Democracy", "political_system", 
              "Government by the people")
kb.connect_concepts("Democracy", "Freedom", "requires")
kb.visualize()  # Creates PNG visualization
```

### Metacognition Space
Implements dual-process thinking: fast intuitive responses (System 1) and slow deliberate reasoning (System 2).

```python
from life import MetacognitionSpace

mind = MetacognitionSpace(kb)
answer = mind.process_question("What is democracy?")
# Automatically decides: fast answer or deep thinking?
```

### Ideology Framework
Analyze situations from multiple ideological perspectives.

```python
from life import IdeologyFramework

ideology = IdeologyFramework()
ideology.teach_ideology("Libertarianism", 
                       core_values={"freedom": 0.95, "limited_gov": 0.90},
                       principles=["Minimize government intervention"])

analysis = ideology.analyze_from_perspective(
    "Government proposes new regulations",
    "Libertarianism"
)
```

## 🎓 Teaching the System

Life learns through conversation, not training data:

```python
# Teach a concept
kb.add_concept("Capitalism", "economic_system",
              "Private ownership and free markets")

# Create relationships
kb.connect_concepts("Capitalism", "Freedom", "requires")
kb.connect_concepts("Capitalism", "Democracy", "compatible_with")

# The system now understands these connections
answer = mind.process_question(
    "How does capitalism relate to freedom?"
)
# Answer traces through the concept graph relationships
```

## 🔬 Why This Works

| Aspect | Neural Networks | Conceptual Intelligence |
|--------|----------------|------------------------|
| **Learning** | Millions of examples | 3-5 examples |
| **Understanding** | Pattern matching | True comprehension |
| **Reasoning** | Black box | Fully transparent |
| **Correction** | Retrain model | Edit one concept |
| **Hardware** | GPU clusters | Laptop CPU |
| **Explainability** | Difficult/impossible | Built-in |

## 📖 Examples

### Basic Concept Learning
```python
from life import ConceptGraph, MetacognitionSpace

# Create knowledge base
kb = ConceptGraph()

# Teach political concepts
kb.add_concept("Democracy", "political_system", 
              "Government by elected representatives")
kb.add_concept("Freedom", "value", "Power to act without constraint")
kb.connect_concepts("Democracy", "Freedom", "requires")

# Create thinking space
mind = MetacognitionSpace(kb)

# Ask questions
print(mind.process_question("What is democracy?"))
print(mind.process_question("How does democracy relate to freedom?"))
```

### Ideological Analysis
```python
from life import IdeologyFramework

ideologies = IdeologyFramework()

# Teach libertarian perspective
ideologies.teach_ideology("Libertarianism",
    core_values={"individual_freedom": 0.95, "property_rights": 0.90},
    principles=["Minimize government intervention",
               "Voluntary exchange is paramount"])

# Teach socialist perspective
ideologies.teach_ideology("Socialism",
    core_values={"equality": 0.95, "collective_welfare": 0.90},
    principles=["Collective ownership of production",
               "Equitable wealth distribution"])

# Analyze situation from both perspectives
situation = "Government proposes universal basic income"
comparison = ideologies.compare_perspectives(
    situation, 
    ["Libertarianism", "Socialism"]
)
print(comparison)
```

### Visual Reasoning
```python
# Find reasoning paths between concepts
path = kb.find_path("Capitalism", "Equality")
print(path)  # Shows connection chain

# Visualize the entire knowledge structure
kb.visualize("my_worldview.png")
```

## 🗺️ Roadmap

**Phase 1: Foundation (Current)**
- ✅ Concept graph representation
- ✅ Basic metacognition (System 1/2)
- ✅ Ideology framework
- ✅ Visual reasoning

**Phase 2: Advanced Reasoning (Q1 2026)**
- [ ] Multi-hop inference
- [ ] Analogical reasoning
- [ ] Counterfactual thinking
- [ ] Belief revision mechanisms

**Phase 3: Learning Enhancement (Q2 2026)**
- [ ] One-shot concept learning
- [ ] Hypothesis generation
- [ ] Pattern abstraction
- [ ] Conceptual blending

**Phase 4: Integration (Q3 2026)**
- [ ] Natural language interface
- [ ] Web interface for visualization
- [ ] Multi-agent collaboration
- [ ] Knowledge base import/export

**Phase 5: Sovereignty (Q4 2026)**
- [ ] Distributed deployment
- [ ] Decentralized knowledge sharing
- [ ] Privacy-preserving reasoning
- [ ] Self-hosted infrastructure

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Key areas:
- **Core reasoning**: Improve metacognition and inference
- **Knowledge representation**: New graph structures
- **Ideology frameworks**: Add more perspectives
- **Examples**: Show novel use cases
- **Documentation**: Improve clarity

## 📄 License

Apache 2.0 - See [LICENSE](LICENSE) for details.

Core innovations (Concept Graph, Metacognition Space, Ideology Framework) are open source. You're free to use, modify, and distribute.

## 🌟 Inspiration

Life is inspired by:
- **Cognitive architectures**: SOAR, ACT-R, CLARION
- **Knowledge graphs**: Neo4j, semantic networks
- **Philosophy**: Epistemology, belief systems
- **Human reasoning**: Dual-process theory
- **Sovereignty**: Independent, transparent intelligence

Built as a separate project from [AkhAI](https://github.com/algoq369/akhai), sharing the vision of sovereign, transparent intelligence.

## 📬 Contact

Questions? Ideas? Open an issue or discussion.

---

*"The best intelligence system is one you can explain to a 10-year-old."*

**Start building genuine understanding today.**
