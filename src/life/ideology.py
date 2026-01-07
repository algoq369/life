"""
Ideology Module

Learns and reasons from different ideological perspectives.
Each ideology is represented as value hierarchies + reasoning principles.
"""

from typing import Dict, List, Any, Optional


class IdeologyFramework:
    """
    Learns and reasons from different ideological perspectives.
    
    Ideologies are encoded as:
    - Core values with importance weights
    - Reasoning principles (rules/beliefs)
    - Example situations
    
    Example:
        >>> ideology = IdeologyFramework()
        >>> ideology.teach_ideology("Libertarianism",
        ...     core_values={"freedom": 0.95, "limited_gov": 0.90},
        ...     principles=["Minimize government intervention"])
        >>> analysis = ideology.analyze_from_perspective(
        ...     "New regulation proposed", "Libertarianism")
    """
    
    def __init__(self):
        """Initialize empty ideology framework"""
        self.ideologies: Dict[str, Dict[str, Any]] = {}
    
    def teach_ideology(
        self,
        name: str,
        core_values: Dict[str, float],
        principles: List[str],
        description: str = "",
        examples: Optional[List[str]] = None
    ) -> None:
        """
        Teach a new ideological framework
        
        Args:
            name: Ideology name (e.g., "Libertarianism")
            core_values: Dictionary of {value: importance} (0-1)
            principles: List of rules/beliefs as strings
            description: Optional overview
            examples: Optional list of case studies
            
        Example:
            >>> ideology.teach_ideology(
            ...     "Socialism",
            ...     core_values={"equality": 0.95, "collective_welfare": 0.90},
            ...     principles=["Collective ownership of production"],
            ...     description="Economic system emphasizing equality"
            ... )
        """
        if not all(0 <= v <= 1 for v in core_values.values()):
            raise ValueError("Core values must be between 0 and 1")
        
        self.ideologies[name] = {
            "values": core_values,
            "principles": principles,
            "description": description,
            "examples": examples or []
        }
        print(f"✓ Learned ideology: {name}")
    
    def analyze_from_perspective(
        self, 
        situation: str, 
        ideology_name: str
    ) -> str:
        """
        Analyze situation through ideological lens
        
        Args:
            situation: Description of situation to analyze
            ideology_name: Which ideology to use
            
        Returns:
            Analysis string with value assessment and recommendations
        """
        if ideology_name not in self.ideologies:
            return f"I haven't learned about {ideology_name} yet."
        
        ideology = self.ideologies[ideology_name]
        
        analysis = f"\n{'='*60}\n"
        analysis += f"🎭 {ideology_name} Perspective\n"
        analysis += f"{'='*60}\n\n"
        
        if ideology.get('description'):
            analysis += f"Overview: {ideology['description']}\n\n"
        
        # Core values (sorted by importance)
        analysis += "Core Values (by priority):\n"
        sorted_values = sorted(
            ideology['values'].items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        for value, importance in sorted_values:
            bar = '█' * int(importance * 10)
            analysis += f"  • {value:<20} {bar} {importance:.2f}\n"
        
        analysis += f"\n📋 Situation: {situation}\n\n"
        
        # Value impact assessment
        analysis += "Value Impact Assessment:\n"
        for value, importance in sorted_values:
            impact = self._assess_value_impact(situation, value)
            analysis += f"  • {value}: {impact}\n"
        
        # Apply principles
        analysis += "\nRelevant Principles:\n"
        for i, principle in enumerate(ideology['principles'], 1):
            analysis += f"  {i}. {principle}\n"
        
        # Generate recommendation
        recommendation = self._generate_recommendation(
            situation, 
            ideology['values'], 
            ideology['principles']
        )
        analysis += f"\n💡 Recommendation:\n{recommendation}\n"
        
        return analysis
    
    def compare_perspectives(
        self, 
        situation: str, 
        ideologies_to_compare: List[str]
    ) -> str:
        """
        Compare how different ideologies view the same situation
        
        Args:
            situation: Situation to analyze
            ideologies_to_compare: List of ideology names
            
        Returns:
            Comparative analysis string
        """
        comparison = f"\n{'='*60}\n"
        comparison += "🔄 Multi-Perspective Analysis\n"
        comparison += f"{'='*60}\n"
        comparison += f"\n📋 Situation: {situation}\n\n"
        
        for ideology in ideologies_to_compare:
            if ideology in self.ideologies:
                comparison += self.analyze_from_perspective(situation, ideology)
                comparison += "\n" + "-"*60 + "\n"
        
        # Add synthesis
        comparison += "\n🎯 Synthesis:\n"
        comparison += self._synthesize_perspectives(
            situation, 
            ideologies_to_compare
        )
        
        return comparison
    
    def _assess_value_impact(self, situation: str, value: str) -> str:
        """
        Assess how situation impacts a particular value
        
        Args:
            situation: Situation description
            value: Value to assess
            
        Returns:
            Impact description
        """
        # Simple keyword matching heuristic
        situation_lower = situation.lower()
        value_lower = value.lower()
        
        # Direct mention
        if value_lower in situation_lower:
            return "Directly affected ⚠️"
        
        # Related keywords
        value_keywords = {
            "freedom": ["liberty", "choice", "autonomy"],
            "equality": ["equal", "fair", "equitable"],
            "security": ["safe", "protect", "stability"],
            "property": ["ownership", "private", "assets"],
            "collective": ["common", "shared", "together"]
        }
        
        keywords = value_keywords.get(value_lower, [])
        if any(kw in situation_lower for kw in keywords):
            return "Indirectly impacted ⚡"
        
        return "Minimal impact ○"
    
    def _generate_recommendation(
        self, 
        situation: str, 
        values: Dict[str, float], 
        principles: List[str]
    ) -> str:
        """
        Generate action recommendation based on ideology
        
        Args:
            situation: Situation description
            values: Core values with weights
            principles: Reasoning principles
            
        Returns:
            Recommendation text
        """
        # Simple heuristic-based recommendation
        situation_lower = situation.lower()
        
        # Check for government/regulation keywords
        if any(word in situation_lower for word in ['government', 'regulation', 'law', 'mandate']):
            if values.get('limited_government', 0) > 0.7 or values.get('freedom', 0) > 0.8:
                return "  → Oppose government intervention. Preserve individual freedom and voluntary action."
            elif values.get('collective_welfare', 0) > 0.7 or values.get('equality', 0) > 0.8:
                return "  → Support if it promotes collective welfare and reduces inequality."
        
        # Check for economic keywords
        if any(word in situation_lower for word in ['economy', 'market', 'business', 'wealth']):
            if values.get('free_markets', 0) > 0.7:
                return "  → Let markets operate freely. Minimize restrictions on economic activity."
            elif values.get('equality', 0) > 0.8:
                return "  → Ensure economic decisions promote equitable distribution."
        
        # Default recommendation based on top value
        top_value = max(values.items(), key=lambda x: x[1])[0]
        return f"  → Prioritize {top_value} in decision-making process."
    
    def _synthesize_perspectives(
        self, 
        situation: str, 
        ideologies: List[str]
    ) -> str:
        """
        Synthesize insights across multiple perspectives
        
        Args:
            situation: Situation description
            ideologies: List of ideology names
            
        Returns:
            Synthesis text
        """
        valid_ideologies = [i for i in ideologies if i in self.ideologies]
        
        if not valid_ideologies:
            return "No valid ideologies to synthesize."
        
        synthesis = "Different perspectives reveal:\n"
        
        # Collect all unique values
        all_values = set()
        for ideology in valid_ideologies:
            all_values.update(self.ideologies[ideology]['values'].keys())
        
        synthesis += f"  • {len(all_values)} distinct values at play\n"
        synthesis += f"  • {len(valid_ideologies)} competing frameworks\n"
        synthesis += "  • Decision requires balancing trade-offs\n\n"
        
        synthesis += "Consider: What values matter most in this specific context?"
        
        return synthesis
    
    def get_ideology(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve ideology data
        
        Args:
            name: Ideology name
            
        Returns:
            Ideology dictionary or None if not found
        """
        return self.ideologies.get(name)
    
    def list_ideologies(self) -> List[str]:
        """
        Get list of all learned ideologies
        
        Returns:
            List of ideology names
        """
        return list(self.ideologies.keys())
    
    def remove_ideology(self, name: str) -> bool:
        """
        Remove an ideology from the framework
        
        Args:
            name: Ideology to remove
            
        Returns:
            True if removed, False if not found
        """
        if name in self.ideologies:
            del self.ideologies[name]
            print(f"✓ Removed ideology: {name}")
            return True
        return False
    
    def export_ideologies(self, filename: str) -> None:
        """
        Export all ideologies to JSON file
        
        Args:
            filename: Output filename
        """
        import json
        with open(filename, 'w') as f:
            json.dump(self.ideologies, f, indent=2)
        print(f"💾 Ideologies exported to: {filename}")
    
    def import_ideologies(self, filename: str) -> None:
        """
        Import ideologies from JSON file
        
        Args:
            filename: Input filename
        """
        import json
        with open(filename, 'r') as f:
            self.ideologies = json.load(f)
        print(f"📂 Ideologies imported from: {filename}")
    
    def __repr__(self) -> str:
        return f"IdeologyFramework(ideologies={len(self.ideologies)})"
