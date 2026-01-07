"""
Metacognition Module

Implements System 1 (fast, intuitive) and System 2 (slow, deliberate) thinking.
Provides a "thinking space" where AI reflects before responding.
"""

from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
from life.concept_graph import ConceptGraph


class MetacognitionSpace:
    """
    The 'thinking space' where AI reflects before responding.
    
    Implements dual-process thinking:
    - System 1: Fast, intuitive, pattern-based
    - System 2: Slow, deliberate, analytical
    
    Example:
        >>> kb = ConceptGraph()
        >>> # ... add concepts ...
        >>> mind = MetacognitionSpace(kb)
        >>> answer = mind.process_question("What is democracy?")
    """
    
    def __init__(
        self, 
        knowledge_graph: ConceptGraph,
        confidence_threshold: float = 0.7
    ):
        """
        Initialize metacognition space
        
        Args:
            knowledge_graph: ConceptGraph instance to reason over
            confidence_threshold: Minimum confidence for fast answers (0-1)
        """
        self.kb = knowledge_graph
        self.confidence_threshold = confidence_threshold
        self.thinking_log: List[Dict[str, Any]] = []
    
    def process_question(self, question: str) -> str:
        """
        Main thinking loop - decides between fast/slow reasoning
        
        Args:
            question: User's question
            
        Returns:
            Answer string with reasoning
        """
        print(f"\n❓ Question: {question}")
        print("="*60)
        
        # System 1: Quick check
        quick_answer, confidence = self._fast_thinking(question)
        
        if confidence > self.confidence_threshold:
            print(f"💨 Fast answer (confidence: {confidence:.2f})")
            return quick_answer
        
        # System 2: Deep thinking
        print(f"🤔 Low confidence ({confidence:.2f}). Entering deep thinking mode...")
        return self._slow_thinking(question)
    
    def _fast_thinking(self, question: str) -> Tuple[str, float]:
        """
        System 1: Immediate, intuitive response
        
        Args:
            question: User's question
            
        Returns:
            Tuple of (answer, confidence_score)
        """
        # Simple keyword matching to find relevant concepts
        words = self._extract_keywords(question)
        
        relevant_concepts = []
        for node in self.kb.graph.nodes():
            if any(word in node.lower() for word in words):
                relevant_concepts.append(node)
        
        if not relevant_concepts:
            return "I don't know yet.", 0.0
        
        # If we found concepts, explain them
        if len(relevant_concepts) == 1:
            return self.kb.explain_concept(relevant_concepts[0]), 0.8
        
        # Multiple concepts - lower confidence, need synthesis
        answer = "\n".join([
            self.kb.explain_concept(c) 
            for c in relevant_concepts[:3]  # Limit to top 3
        ])
        return answer, 0.5
    
    def _slow_thinking(self, question: str) -> str:
        """
        System 2: Deliberate, analytical reasoning
        
        Args:
            question: User's question
            
        Returns:
            Synthesized answer with reasoning chain
        """
        # Log thinking process
        self.thinking_log.append({
            "question": question,
            "timestamp": datetime.now().isoformat(),
            "mode": "deep_thinking"
        })
        
        # Step 1: Identify all relevant concepts
        words = self._extract_keywords(question)
        relevant = [
            n for n in self.kb.graph.nodes() 
            if any(w in n.lower() for w in words)
        ]
        
        if not relevant:
            return self._generate_learning_request(question)
        
        # Step 2: Find connections between concepts
        reasoning_chain = []
        
        # Explain each relevant concept
        for concept in relevant:
            reasoning_chain.append(self.kb.explain_concept(concept))
        
        # Find paths between concepts
        for i, concept in enumerate(relevant):
            for other in relevant[i+1:]:
                path = self.kb.find_path(concept, other)
                if "No connection" not in path:
                    reasoning_chain.append(path)
        
        # Step 3: Synthesize answer
        answer = "\n🧠 Deep Analysis:\n"
        answer += "\n".join(reasoning_chain)
        
        return answer
    
    def _extract_keywords(self, question: str) -> List[str]:
        """
        Extract meaningful keywords from question
        
        Args:
            question: User's question
            
        Returns:
            List of lowercase keywords
        """
        # Remove common stop words and punctuation
        stop_words = {
            'what', 'is', 'are', 'the', 'a', 'an', 'how', 'does', 
            'do', 'can', 'could', 'would', 'should', 'about', 'to'
        }
        
        words = question.lower().replace('?', '').replace(',', '').split()
        return [w for w in words if w not in stop_words and len(w) > 2]
    
    def _generate_learning_request(self, question: str) -> str:
        """
        Generate helpful response when knowledge is insufficient
        
        Args:
            question: Original question
            
        Returns:
            Learning request message
        """
        return (
            f"I need more knowledge to answer: '{question}'\n\n"
            "Can you teach me the relevant concepts? Use:\n"
            "  kb.add_concept(name, type, definition)\n"
            "  kb.connect_concepts(concept1, concept2, relationship)"
        )
    
    def analyze_confidence(self, question: str) -> Dict[str, Any]:
        """
        Analyze confidence without generating full answer
        
        Args:
            question: User's question
            
        Returns:
            Dictionary with confidence analysis
        """
        _, confidence = self._fast_thinking(question)
        words = self._extract_keywords(question)
        
        relevant = [
            n for n in self.kb.graph.nodes() 
            if any(w in n.lower() for w in words)
        ]
        
        return {
            "confidence": confidence,
            "will_use_system": 1 if confidence > self.confidence_threshold else 2,
            "relevant_concepts_found": len(relevant),
            "keywords_extracted": words
        }
    
    def get_thinking_log(self) -> List[Dict[str, Any]]:
        """
        Retrieve history of thinking processes
        
        Returns:
            List of thinking log entries
        """
        return self.thinking_log.copy()
    
    def clear_log(self) -> None:
        """Clear thinking history"""
        self.thinking_log = []
    
    def set_confidence_threshold(self, threshold: float) -> None:
        """
        Adjust confidence threshold for System 1/2 decision
        
        Args:
            threshold: New threshold value (0-1)
        """
        if not 0 <= threshold <= 1:
            raise ValueError("Threshold must be between 0 and 1")
        self.confidence_threshold = threshold
        print(f"✓ Confidence threshold set to: {threshold:.2f}")
    
    def __repr__(self) -> str:
        return (f"MetacognitionSpace("
                f"concepts={self.kb.graph.number_of_nodes()}, "
                f"threshold={self.confidence_threshold:.2f})")
