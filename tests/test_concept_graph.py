"""
Tests for ConceptGraph module
"""

import pytest
from life import ConceptGraph


class TestConceptGraph:
    """Test suite for ConceptGraph class"""
    
    def test_initialization(self):
        """Test ConceptGraph can be initialized"""
        kb = ConceptGraph()
        assert kb.graph.number_of_nodes() == 0
        assert kb.graph.number_of_edges() == 0
    
    def test_add_concept(self):
        """Test adding a concept to the graph"""
        kb = ConceptGraph()
        kb.add_concept("Democracy", "political_system", "Government by the people")
        
        assert "Democracy" in kb.graph.nodes()
        assert kb.graph.nodes["Democracy"]["type"] == "political_system"
        assert kb.graph.nodes["Democracy"]["definition"] == "Government by the people"
    
    def test_connect_concepts(self):
        """Test creating relationships between concepts"""
        kb = ConceptGraph()
        kb.add_concept("Democracy", "political_system")
        kb.add_concept("Freedom", "value")
        kb.connect_concepts("Democracy", "Freedom", "requires")
        
        assert kb.graph.has_edge("Democracy", "Freedom")
        assert kb.graph["Democracy"]["Freedom"]["relationship"] == "requires"
    
    def test_get_concept(self):
        """Test retrieving concept data"""
        kb = ConceptGraph()
        kb.add_concept("Freedom", "value", "Power to act without constraint")
        
        concept = kb.get_concept("Freedom")
        assert concept is not None
        assert concept["type"] == "value"
        assert concept["definition"] == "Power to act without constraint"
    
    def test_get_nonexistent_concept(self):
        """Test retrieving concept that doesn't exist"""
        kb = ConceptGraph()
        concept = kb.get_concept("NonExistent")
        assert concept is None
    
    def test_explain_concept(self):
        """Test concept explanation generation"""
        kb = ConceptGraph()
        kb.add_concept("Democracy", "political_system", "Government by the people")
        
        explanation = kb.explain_concept("Democracy")
        assert "Democracy" in explanation
        assert "Government by the people" in explanation
    
    def test_explain_nonexistent_concept(self):
        """Test explanation for concept that doesn't exist"""
        kb = ConceptGraph()
        explanation = kb.explain_concept("NonExistent")
        assert "haven't learned" in explanation
    
    def test_find_path(self):
        """Test finding reasoning path between concepts"""
        kb = ConceptGraph()
        kb.add_concept("A", "type")
        kb.add_concept("B", "type")
        kb.add_concept("C", "type")
        kb.connect_concepts("A", "B", "relates_to")
        kb.connect_concepts("B", "C", "leads_to")
        
        path = kb.find_path("A", "C")
        assert "A" in path
        assert "B" in path
        assert "C" in path
    
    def test_get_statistics(self):
        """Test graph statistics"""
        kb = ConceptGraph()
        kb.add_concept("A", "type1")
        kb.add_concept("B", "type2")
        kb.connect_concepts("A", "B", "relates_to")
        
        stats = kb.get_statistics()
        assert stats["total_concepts"] == 2
        assert stats["total_relationships"] == 1
        assert stats["concept_types"] >= 2


class TestConceptGraphRelationships:
    """Test suite for relationship features"""
    
    def test_get_related_concepts(self):
        """Test finding related concepts"""
        kb = ConceptGraph()
        kb.add_concept("Center", "type")
        kb.add_concept("Related1", "type")
        kb.add_concept("Related2", "type")
        kb.connect_concepts("Center", "Related1", "connects_to")
        kb.connect_concepts("Center", "Related2", "connects_to")
        
        related = kb.get_related_concepts("Center", depth=1)
        assert "Related1" in related
        assert "Related2" in related
    
    def test_bidirectional_relationships(self):
        """Test that relationships can be queried in both directions"""
        kb = ConceptGraph()
        kb.add_concept("A", "type")
        kb.add_concept("B", "type")
        kb.connect_concepts("A", "B", "requires")
        
        # Forward
        assert kb.graph.has_edge("A", "B")
        # Should be able to find predecessors of B
        predecessors = list(kb.graph.predecessors("B"))
        assert "A" in predecessors


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
