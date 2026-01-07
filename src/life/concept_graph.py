"""
Concept Graph Module

Visual knowledge representation as networks of connected concepts.
Implements graph-based knowledge storage with relationship tracking.
"""

import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any


class ConceptGraph:
    """
    Visual knowledge representation as a network of connected concepts.
    
    Concepts are nodes with attributes, relationships are directed edges.
    Supports querying, path finding, and visualization.
    
    Example:
        >>> kb = ConceptGraph()
        >>> kb.add_concept("Democracy", "political_system", 
        ...                "Government by the people")
        >>> kb.connect_concepts("Democracy", "Freedom", "requires")
        >>> kb.visualize()
    """
    
    def __init__(self):
        """Initialize empty concept graph"""
        self.graph = nx.DiGraph()
        
    def add_concept(
        self, 
        name: str, 
        concept_type: str = "general",
        definition: str = "", 
        **attributes: Any
    ) -> None:
        """
        Teach the AI a new concept
        
        Args:
            name: Unique concept identifier
            concept_type: Category (e.g., "value", "system", "mechanism")
            definition: Text definition
            **attributes: Additional key-value attributes
            
        Example:
            >>> kb.add_concept("Freedom", "value",
            ...                "Power to act without constraint",
            ...                importance=0.9)
        """
        self.graph.add_node(
            name,
            type=concept_type,
            definition=definition,
            learned_at=datetime.now().isoformat(),
            **attributes
        )
        print(f"✓ Learned concept: {name} ({concept_type})")
    
    def connect_concepts(
        self, 
        from_concept: str, 
        to_concept: str, 
        relationship: str = "relates_to"
    ) -> None:
        """
        Create a relationship between two concepts
        
        Args:
            from_concept: Source concept name
            to_concept: Target concept name
            relationship: Nature of relationship (e.g., "requires", "enables")
            
        Example:
            >>> kb.connect_concepts("Democracy", "Voting", "enables")
        """
        if from_concept not in self.graph or to_concept not in self.graph:
            print(f"⚠ One or both concepts not found. Teach them first!")
            return
        
        self.graph.add_edge(from_concept, to_concept, relationship=relationship)
        print(f"✓ Connected: {from_concept} --[{relationship}]--> {to_concept}")
    
    def get_concept(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve concept data
        
        Args:
            name: Concept name
            
        Returns:
            Dictionary of concept attributes or None if not found
        """
        if name not in self.graph:
            return None
        return dict(self.graph.nodes[name])
    
    def explain_concept(self, concept: str) -> str:
        """
        Generate explanation from graph structure
        
        Args:
            concept: Concept name to explain
            
        Returns:
            Human-readable explanation with relationships
        """
        if concept not in self.graph:
            return f"I haven't learned about '{concept}' yet. Can you teach me?"
        
        # Get concept data
        attrs = self.graph.nodes[concept]
        
        # Get relationships
        outgoing = [
            (target, self.graph[concept][target]['relationship']) 
            for target in self.graph.successors(concept)
        ]
        incoming = [
            (source, self.graph[source][concept]['relationship']) 
            for source in self.graph.predecessors(concept)
        ]
        
        # Build explanation
        explanation = f"\n{'='*50}\n"
        explanation += f"📖 {concept}\n"
        explanation += f"{'='*50}\n\n"
        
        if attrs.get('definition'):
            explanation += f"Definition: {attrs['definition']}\n\n"
        
        if outgoing:
            explanation += "This concept:\n"
            for target, rel in outgoing:
                explanation += f"  • {rel} → {target}\n"
            explanation += "\n"
        
        if incoming:
            explanation += "Related from:\n"
            for source, rel in incoming:
                explanation += f"  • {source} --[{rel}]→ this\n"
        
        return explanation
    
    def find_path(
        self, 
        from_concept: str, 
        to_concept: str
    ) -> str:
        """
        Find reasoning path between two concepts
        
        Args:
            from_concept: Starting concept
            to_concept: Target concept
            
        Returns:
            String describing the reasoning path
        """
        try:
            path = nx.shortest_path(self.graph, from_concept, to_concept)
            reasoning = f"\n🔗 Reasoning path from '{from_concept}' to '{to_concept}':\n"
            
            for i in range(len(path) - 1):
                source = path[i]
                target = path[i + 1]
                rel = self.graph[source][target]['relationship']
                reasoning += f"  {source} --[{rel}]--> {target}\n"
            
            return reasoning
        except nx.NetworkXNoPath:
            return f"No connection found between '{from_concept}' and '{to_concept}'"
        except nx.NodeNotFound as e:
            return f"Concept not found: {e}"
    
    def get_related_concepts(
        self, 
        concept: str, 
        depth: int = 1
    ) -> List[str]:
        """
        Get all concepts within specified depth
        
        Args:
            concept: Starting concept
            depth: Maximum relationship hops
            
        Returns:
            List of related concept names
        """
        if concept not in self.graph:
            return []
        
        related = set()
        
        # Get all nodes within depth using BFS
        for node, dist in nx.single_source_shortest_path_length(
            self.graph.to_undirected(), concept, cutoff=depth
        ).items():
            if node != concept:
                related.add(node)
        
        return list(related)
    
    def visualize(
        self, 
        filename: str = "knowledge_graph.png",
        figsize: Tuple[int, int] = (12, 8)
    ) -> None:
        """
        Create visual representation of concept graph
        
        Args:
            filename: Output filename
            figsize: Figure dimensions (width, height)
        """
        plt.figure(figsize=figsize)
        pos = nx.spring_layout(self.graph, k=2, iterations=50)
        
        # Draw nodes
        nx.draw_networkx_nodes(
            self.graph, pos, 
            node_color='lightblue',
            node_size=3000,
            alpha=0.9
        )
        
        # Draw labels
        nx.draw_networkx_labels(
            self.graph, pos, 
            font_size=10,
            font_weight='bold'
        )
        
        # Draw edges with arrows
        nx.draw_networkx_edges(
            self.graph, pos,
            edge_color='gray',
            arrows=True,
            arrowsize=20,
            width=2
        )
        
        # Draw edge labels (relationships)
        edge_labels = nx.get_edge_attributes(self.graph, 'relationship')
        nx.draw_networkx_edge_labels(
            self.graph, pos, edge_labels,
            font_size=8
        )
        
        plt.title("Knowledge Graph Visualization", fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"\n💾 Visualization saved to: {filename}")
        plt.close()
    
    def export_graph(self, filename: str) -> None:
        """
        Export graph to JSON format
        
        Args:
            filename: Output JSON filename
        """
        import json
        from networkx.readwrite import json_graph
        
        data = json_graph.node_link_data(self.graph)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"💾 Graph exported to: {filename}")
    
    def import_graph(self, filename: str) -> None:
        """
        Import graph from JSON format
        
        Args:
            filename: Input JSON filename
        """
        import json
        from networkx.readwrite import json_graph
        
        with open(filename, 'r') as f:
            data = json.load(f)
        self.graph = json_graph.node_link_graph(data)
        print(f"📂 Graph imported from: {filename}")
    
    def get_statistics(self) -> Dict[str, int]:
        """
        Get graph statistics
        
        Returns:
            Dictionary with concept count, relationship count, etc.
        """
        return {
            "total_concepts": self.graph.number_of_nodes(),
            "total_relationships": self.graph.number_of_edges(),
            "concept_types": len(set(
                attrs.get('type', 'unknown') 
                for _, attrs in self.graph.nodes(data=True)
            ))
        }
    
    def __repr__(self) -> str:
        stats = self.get_statistics()
        return (f"ConceptGraph("
                f"concepts={stats['total_concepts']}, "
                f"relationships={stats['total_relationships']})")
