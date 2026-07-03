def health():
    return {
        "application": "Git DevOps Workflow Demo",
        "status": "Running",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    print(health())
