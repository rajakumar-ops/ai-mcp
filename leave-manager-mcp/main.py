from mcp.server.fastmcp import FastMCP
from typing import List

employee_leaves = {
    "Alice": {
        "balance": 15,
        "history": ["2023-01-10", "2023-02-15", "2023-05-22"]
    },
    "Bob": {
        "balance": 20,
        "history": ["2023-03-05", "2023-04-18"]
    }
}


mcp = FastMCP("LeaveManager")




@mcp.tool()
def get_employee_leaves(employee_name: str = None) -> dict:
    """Get leave information for a specific employee or all employees.
    
    Args:
        employee_name: Name of employee to get leave information for. If None, returns all employees.
        
    Returns:
        Dictionary containing leave information.
    """
    if employee_name:
        if employee_name in employee_leaves:
            return {employee_name: employee_leaves[employee_name]}
        return {"error": f"Employee {employee_name} not found"}
    return employee_leaves

if __name__ == "__main__":
    mcp.run()