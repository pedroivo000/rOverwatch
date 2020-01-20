#Helper functions

clean_self_text <- function(df) {
  df %>%
    filter(
      !nchar(selftext)==0, #remove empty texts
      !str_detect(selftext, "\\[removed\\]"),  #remove [removed],
      !str_detect(selftext, "\\[deleted\\]"), #remove [deleted]
      !str_detect(selftext, "^&amp"), #remove links
      !str_detect(selftext, "^\\[http*") #remove more links
    )
}