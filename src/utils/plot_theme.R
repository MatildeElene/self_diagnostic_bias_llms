

# Shared palette
col_male   <- "#c9cba3"
col_female <- "#ffe1a8"
col_proxy  <- "#FC6E51"
col_male_proxy   <- "#F6BD60"
col_female_proxy <- "#F28482"

# Shared ggplot theme
theme_paper <- function() {
  ggplot2::theme_minimal(base_family = "serif") +
    ggplot2::theme(
      plot.title = ggplot2::element_text(
        face = "bold",
        hjust = 0.5,
        size = 10
      ),
      plot.subtitle = ggplot2::element_text(
        face = "italic",
        hjust = 0.5,
        size = 9
      ),
      axis.title = ggplot2::element_text(size = 9),
      axis.text = ggplot2::element_text(size = 8.5),
      panel.grid.minor = ggplot2::element_blank(),
      panel.grid.major.x = ggplot2::element_blank(),
      panel.grid.major.y = ggplot2::element_line(
        color = grDevices::adjustcolor("#BDBDBD", alpha.f = 0.2),
        linewidth = 0.4
      ),
      axis.line = ggplot2::element_line(linewidth = 0.1),
      axis.ticks = ggplot2::element_line(linewidth = 0.6),
      legend.position = "top"
    )
}

# Shared gt table theme
theme_gt_paper <- function(gt_obj) {
  gt_obj %>%
    gt::tab_options(
      table.width = gt::pct(70),
      data_row.padding = gt::px(18),
      column_labels.padding = gt::px(8),
      table.border.top.width = gt::px(1),
      table.border.bottom.width = gt::px(1),
      heading.border.bottom.width = gt::px(1),
      column_labels.border.bottom.width = gt::px(1)
    ) %>%
    gt::cols_align(
      align = "center",
      columns = dplyr::everything()
    ) %>%
    gt::tab_style(
      style = list(
        gt::cell_text(weight = "bold"),
        gt::cell_fill(
          color = grDevices::adjustcolor(col_male, alpha.f = 0.2)
        )
      ),
      locations = gt::cells_column_labels(dplyr::everything())
    ) %>%
    gt::tab_style(
      style = gt::cell_text(style = "italic", size = gt::px(16)),
      locations = gt::cells_title(groups = "subtitle")
    )
}