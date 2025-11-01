# Copilot Instructions for ELT Data Modeling Repository

This repository focuses on ELT (Extract, Load, Transform) data modeling patterns and best practices.

## Project Overview

This is a data engineering project that implements ELT data modeling principles. When working on this repository, keep in mind:

- **ELT** means Extract, Load, Transform - data is loaded first, then transformed in the target system
- Focus on modern data warehouse and lakehouse architectures
- Emphasize SQL-based transformations and data modeling best practices

## Code Style and Conventions

### SQL
- Use lowercase for SQL keywords (e.g., `select`, `from`, `where`)
- Use snake_case for table and column names
- Include descriptive comments for complex queries
- Follow dimensional modeling principles (facts and dimensions)
- Organize transformations into logical layers: staging, intermediate, and mart

### Python (if applicable)
- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Write docstrings for all functions and classes
- Use meaningful variable names

### Documentation
- Update README.md when adding new features or significant changes
- Document data models and their relationships
- Include data lineage information where applicable
- Document transformation logic and business rules

## Testing

When adding or modifying code:

- Write tests for data transformations
- Test edge cases and data quality rules
- Validate schema changes
- Include integration tests for end-to-end pipelines
- Test with sample data when possible

## Build and Deployment

- Ensure all SQL is valid and can be executed in the target environment
- Verify dependencies are correctly specified
- Document any required environment variables or configuration
- Include setup instructions in documentation

## Data Quality

- Implement data quality checks and assertions
- Handle NULL values appropriately
- Document data type expectations
- Add constraints where appropriate
- Consider data freshness and staleness

## Best Practices

- Keep transformations modular and reusable
- Avoid hard-coding values; use configuration or parameters
- Optimize queries for performance
- Document data sources and their refresh schedules
- Follow the principle of least privilege for data access
- Version control all transformation code and data models

## Common Tasks

When asked to:
- **Add a new data model**: Create appropriate staging, intermediate, and mart layers
- **Write a transformation**: Follow the ELT pattern and document the business logic
- **Add tests**: Include unit tests for transformations and data quality checks
- **Update documentation**: Keep README and inline documentation current
- **Optimize queries**: Profile performance and add appropriate indexes or partitioning strategies

## References

- [dbt Best Practices](https://docs.getdbt.com/guides/best-practices)
- [Kimball Dimensional Modeling](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/)
- [The Data Warehouse Toolkit](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/)
