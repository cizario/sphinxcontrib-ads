from sphinx.errors import ConfigError


class AdsConfigError(ConfigError):
    """Ads configuration error. Raised when a value is missing or misconfigured."""
    category = 'Ads config error'
