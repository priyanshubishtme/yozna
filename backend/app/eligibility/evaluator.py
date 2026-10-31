from typing import Dict, Any, List

class EligibilityEvaluator:
    """
    Three-valued deterministic rule evaluator.
    Returns: TRUE, FALSE, or UNKNOWN
    """
    def __init__(self, rules: List[Dict[str, Any]]):
        self.rules = rules

    def evaluate(self, profile: Dict[str, Any]) -> str:
        # Simplified evaluation for demo
        for rule in self.rules:
            field = rule.get("field")
            expected_val = rule.get("value")

            if field not in profile:
                return "UNKNOWN"

            if profile[field] != expected_val:
                return "FALSE"

        return "TRUE"

    def get_status(self, profile: Dict[str, Any]) -> str:
        result = self.evaluate(profile)
        if result == "TRUE":
            return "Eligible"
        elif result == "FALSE":
            return "Not Eligible"
        else:
            return "Need More Information"
