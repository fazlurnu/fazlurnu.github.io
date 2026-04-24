source "https://rubygems.org"

# Plain Jekyll 4 — simpler dependency tree, no eventmachine headaches.
# GitHub Pages will still build the deployed site using its own pinned Jekyll;
# this Gemfile is only for local preview.
gem "jekyll", "~> 4.3"

group :jekyll_plugins do
  gem "jekyll-seo-tag"
  gem "jekyll-feed"
  gem "jekyll-sitemap"
end

gem "wdm", "~> 0.1", platforms: [:mingw, :x64_mingw, :mswin]
gem "tzinfo-data", platforms: [:mingw, :x64_mingw, :mswin, :jruby]
