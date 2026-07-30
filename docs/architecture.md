# Architecture

```
main.py
    │
    ▼
MovieRepository
    │
    ├────────► StatisticsService
    ├────────► SearchService
    ├────────► HistoryService
    ├────────► JsonExporter
    ├────────► CsvExporter
    ├────────► ConsoleRenderer
    └────────► Rating
```

## Components

### Repository

Stores the movie collection.

### Services

Provides search, statistics and history tracking.

### Exporters

Exports the watchlist to JSON and CSV.

### Renderer

Displays formatted output in the console.

### Utils

Contains reusable formatting helpers.
