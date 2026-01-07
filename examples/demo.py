"""
Life: Conceptual Intelligence System - Interactive Demo

Demonstrates teaching concepts, creating relationships,
and reasoning from multiple perspectives.

Install and run:
    pip install -e .
    python examples/demo.py

Or:
    life-demo
"""

from life import ConceptGraph, MetacognitionSpace, IdeologyFramework


def main():
    """
    Interactive demo showing how to teach the system concepts and ideologies
    """
    print("\n" + "="*60)
    print("🎓 LIFE: CONCEPTUAL INTELLIGENCE - DEMO")
    print("="*60 + "\n")
    
    # Create the knowledge graph
    kb = ConceptGraph()
    
    # === TEACH CORE CONCEPTS ===
    print("\n📚 Teaching Core Concepts...\n")
    
    # Political systems
    kb.add_concept("Democracy", "political_system",
                  "Government by the people, through elected representatives")
    kb.add_concept("Authoritarianism", "political_system",
                  "Centralized power with limited individual freedom")
    
    # Values
    kb.add_concept("Freedom", "value",
                  "The power to act, speak, or think without constraint")
    kb.add_concept("Equality", "value",
                  "The state of being equal in status, rights, and opportunities")
    kb.add_concept("Security", "value",
                  "The state of being protected from harm or danger")
    
    # Mechanisms
    kb.add_concept("Voting", "mechanism",
                  "Formal expression of opinion or choice by individuals")
    kb.add_concept("Rule_of_Law", "mechanism",
                  "Legal principle that law should govern rather than arbitrary decisions")
    
    # === CREATE RELATIONSHIPS ===
    print("\n🔗 Creating Relationships...\n")
    
    kb.connect_concepts("Democracy", "Freedom", "requires")
    kb.connect_concepts("Democracy", "Voting", "enables")
    kb.connect_concepts("Democracy", "Equality", "promotes")
    kb.connect_concepts("Democracy", "Rule_of_Law", "depends_on")
    
    kb.connect_concepts("Authoritarianism", "Security", "prioritizes")
    kb.connect_concepts("Authoritarianism", "Freedom", "restricts")
    
    kb.connect_concepts("Voting", "Democracy", "strengthens")
    kb.connect_concepts("Rule_of_Law", "Equality", "enforces")
    
    # === VISUALIZE KNOWLEDGE ===
    print("\n🎨 Creating visual representation...")
    kb.visualize("my_knowledge_graph.png")
    
    # === CREATE METACOGNITION LAYER ===
    print("\n🧠 Initializing metacognition space...")
    mind = MetacognitionSpace(kb)
    
    # === TEACH IDEOLOGIES ===
    print("\n🎭 Teaching Ideological Frameworks...\n")
    
    ideologies = IdeologyFramework()
    
    # Libertarianism
    ideologies.teach_ideology(
        "Libertarianism",
        core_values={
            "individual_freedom": 0.95,
            "property_rights": 0.90,
            "limited_government": 0.85,
            "free_markets": 0.88
        },
        principles=[
            "Government should only protect rights, not grant them",
            "Voluntary exchange maximizes prosperity",
            "Individual choice is paramount",
            "Taxation is coercive force"
        ],
        description="Political philosophy emphasizing individual liberty and minimal government"
    )
    
    # Socialism
    ideologies.teach_ideology(
        "Socialism",
        core_values={
            "equality": 0.95,
            "collective_welfare": 0.90,
            "worker_control": 0.85,
            "reduced_inequality": 0.92
        },
        principles=[
            "Collective ownership of production means",
            "Wealth should be distributed equitably",
            "Society over individual accumulation",
            "Democratic control of economy"
        ],
        description="Economic system emphasizing collective ownership and equality"
    )
    
    # === INTERACTIVE REASONING ===
    print("\n" + "="*60)
    print("💬 INTERACTIVE REASONING SESSION")
    print("="*60)
    
    # Question 1: Simple concept explanation
    print(mind.process_question("What is democracy?"))
    
    # Question 2: Relationship reasoning
    print(mind.process_question("How does voting relate to freedom?"))
    
    # Question 3: Ideological analysis
    situation = "Government proposes universal basic income"
    print(ideologies.compare_perspectives(situation, 
                                         ["Libertarianism", "Socialism"]))
    
    # === DEMONSTRATE LEARNING ===
    print("\n" + "="*60)
    print("📖 TEACHING NEW CONCEPTS")
    print("="*60 + "\n")
    
    # Add new concept based on existing knowledge
    print("Adding 'Capitalism' concept...\n")
    kb.add_concept("Capitalism", "economic_system",
                  "Economic system based on private ownership and free markets")
    kb.connect_concepts("Capitalism", "Freedom", "requires")
    kb.connect_concepts("Capitalism", "Democracy", "compatible_with")
    
    # Show updated reasoning
    print(mind.process_question("What is capitalism and how does it relate to democracy?"))
    
    # === SHOW STATISTICS ===
    print("\n" + "="*60)
    print("📊 KNOWLEDGE BASE STATISTICS")
    print("="*60)
    stats = kb.get_statistics()
    print(f"\nTotal Concepts: {stats['total_concepts']}")
    print(f"Total Relationships: {stats['total_relationships']}")
    print(f"Concept Types: {stats['concept_types']}")
    
    print("\n" + "="*60)
    print("✅ DEMO COMPLETE!")
    print("="*60)
    print("\nYou now have a working conceptual intelligence system that:")
    print("  • Stores knowledge as visual concept graphs")
    print("  • Reasons through relationships")
    print("  • Analyzes from multiple perspectives")
    print("  • Learns through simple teaching")
    print("\nNo neural networks. No gradient descent. Just concepts and reasoning.")
    print("\nVisualization saved as: my_knowledge_graph.png")
    
    print("\n" + "="*60)
    print("🚀 NEXT STEPS")
    print("="*60)
    print("\n1. Examine the generated knowledge graph image")
    print("2. Modify the code to teach YOUR concepts")
    print("3. Add your own ideologies and values")
    print("4. Experiment with different questions")
    print("5. Build your metacognition space further")
    print("\nThis is just the beginning. The system grows with each concept you teach it.")
    print("\nStart building your sovereign intelligence today! 🧠✨\n")


if __name__ == "__main__":
    main()
